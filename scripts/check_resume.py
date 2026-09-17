"""Check layout and committed-PDF freshness; retain renders for human review."""

import argparse
from pathlib import Path
import re

import pymupdf


def links(page):
    return sorted(
        (link.get("kind", 0), link.get("uri", ""), link.get("file", ""),
         link.get("page", -1), str(link.get("to", "")),
         tuple(round(n, 2) for n in link["from"]))
        for link in page.get_links()
    )


def inspect(pdf, output):
    errors = []
    with pymupdf.open(pdf) as document:
        if len(document) != 1:
            errors.append(f"{pdf}: expected one page, found {len(document)}")
        for index, page in enumerate(document):
            page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(
                output / f"{pdf.stem}-{index + 1}.png"
            )
            if abs(page.rect.width - 612) > 1 or abs(page.rect.height - 792) > 1:
                errors.append(f"{pdf}: page {index + 1} must be US Letter")
            if not page.get_text().strip():
                errors.append(f"{pdf}: page {index + 1} has no searchable text")
            # Font bounding boxes extend beyond TeX's nominal margins. Keep a
            # conservative 24pt inset instead of testing exact geometry margins.
            safe = pymupdf.Rect(24, 24, page.rect.width - 24, page.rect.height - 24)
            for block in page.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    for span in line["spans"]:
                        if not span["text"].strip():
                            continue
                        if not safe.contains(pymupdf.Rect(span["bbox"])):
                            errors.append(f"{pdf}: text outside safe bounds: {span['text']!r}")
                        if span["size"] < 9:
                            errors.append(f"{pdf}: text below 9pt: {span['text']!r}")
    return errors


def check(compiled, committed, log, output):
    output.mkdir(parents=True, exist_ok=True)
    errors = []
    log_text = log.read_text(errors="replace")
    if re.search(r"Overfull\s+\\[hv]box|Missing character:", log_text):
        errors.append("LaTeX reported an overfull box or missing glyph; inspect the build log")
    errors.extend(inspect(compiled, output))
    # Separate directories prevent the two identically named PDFs overwriting
    # each other's preview artifacts.
    committed_output = output / "committed"
    committed_output.mkdir(exist_ok=True)
    errors.extend(inspect(committed, committed_output))
    with pymupdf.open(compiled) as fresh, pymupdf.open(committed) as saved:
        if len(fresh) != len(saved):
            errors.append("Committed resume.pdf is stale: page counts differ")
        else:
            for current, previous in zip(fresh, saved):
                a = current.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5))
                b = previous.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5))
                if (a.width, a.height, a.samples) != (b.width, b.height, b.samples):
                    errors.append("Committed resume.pdf is stale: rendered content differs; rebuild it")
                if current.get_text() != previous.get_text() or links(current) != links(previous):
                    errors.append("Committed resume.pdf is stale: text or link targets differ")
    (output / "report.txt").write_text("\n".join(errors) if errors else "All resume checks passed.\n")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compiled", type=Path, default=Path("build/resume.pdf"))
    parser.add_argument("--committed", type=Path, default=Path("resume.pdf"))
    parser.add_argument("--log", type=Path, default=Path("build/resume.log"))
    parser.add_argument("--output", type=Path, default=Path("build/preview"))
    args = parser.parse_args()
    failures = check(args.compiled, args.committed, args.log, args.output)
    print("\n".join(failures) if failures else "All resume checks passed.")
    raise SystemExit(bool(failures))
