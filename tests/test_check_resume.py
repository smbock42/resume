import importlib.util
from pathlib import Path
import tempfile
import unittest

import pymupdf

spec = importlib.util.spec_from_file_location("check_resume", Path(__file__).parents[1] / "scripts/check_resume.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ResumeChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.log = self.root / "resume.log"
        self.log.write_text("Build completed")

    def pdf(self, name, text="Resume example", pages=1, point=(50, 50), size=11,
            uri="mailto:sam@example.com", metadata="", width=612):
        path = self.root / name
        with pymupdf.open() as doc:
            for _ in range(pages):
                page = doc.new_page(width=width, height=792)
                page.insert_text(point, text, fontsize=size)
                page.insert_link({"kind": pymupdf.LINK_URI, "from": pymupdf.Rect(50, 55, 150, 70), "uri": uri})
            doc.set_metadata({"title": metadata})
            doc.save(path)
        return path

    def run_check(self, **changes):
        return module.check(self.pdf("fresh.pdf", **changes), self.pdf("saved.pdf"),
                            self.log, self.root / "preview")

    def test_metadata_only_change_passes_and_renders(self):
        self.assertEqual(self.run_check(metadata="Different metadata"), [])
        self.assertTrue((self.root / "preview/fresh-1.png").is_file())
        self.assertTrue((self.root / "preview/committed/saved-1.png").is_file())

    def test_stale_content_fails(self):
        self.assertTrue(any("rendered content differs" in e for e in self.run_check(text="Changed experience")))

    def test_changed_invisible_link_fails(self):
        self.assertTrue(any("link targets differ" in e for e in self.run_check(uri="https://example.com")))

    def test_second_page_fails(self):
        self.assertTrue(any("expected one page" in e for e in self.run_check(pages=2)))

    def test_margin_overflow_fails(self):
        self.assertTrue(any("outside safe bounds" in e for e in self.run_check(point=(5, 50))))

    def test_small_font_fails(self):
        self.assertTrue(any("below 9pt" in e for e in self.run_check(size=8)))

    def test_wrong_paper_fails(self):
        self.assertTrue(any("US Letter" in e for e in self.run_check(width=595)))

    def test_compiler_overflow_fails(self):
        self.log.write_text(r"Overfull \hbox (8pt too wide) in paragraph")
        self.assertTrue(any("overfull box" in e for e in self.run_check()))

    def test_underfull_box_is_not_failure(self):
        self.log.write_text(r"Underfull \hbox (badness 1000)")
        self.assertEqual(self.run_check(), [])


if __name__ == "__main__":
    unittest.main()
