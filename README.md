# Sam Bock's résumé

Edit `resume.tex`; commit its rebuilt `resume.pdf` in the same pull request.

## Build and check

Use Tectonic 0.17.0 and Python 3.12:

```sh
python -m pip install -r requirements-ci.txt
bash scripts/build_resume.sh
cp build/resume.pdf resume.pdf
python scripts/check_resume.py
python -m unittest discover -s tests -v
```

The build pins the TeX resource bundle to v33 and uses Tectonic's untrusted-input mode. Set `TECTONIC=/path/to/tectonic` when it is not on PATH.

## Pull request checks

`Resume checks / Compile and validate resume` runs on every PR, on main pushes, and manually. It compiles into `build/` without replacing the committed PDF, then checks:

- No overfull horizontal/vertical boxes or missing glyph warnings.
- Exactly one US Letter page with searchable text.
- Text stays within a conservative 24pt page inset and is at least 9pt.
- The committed PDF matches the rebuilt visual content, text and link destinations. PDF timestamps and other metadata do not cause a failure.

Download the `resume-review-<commit>` artifact from the Actions run to inspect the rebuilt PDF, page images, committed-PDF images, compiler log and report. Artifacts are retained for 30 days, including after validation failures when build output exists.

**Human review is still required:** these checks catch common regressions and stale exports, but cannot judge visual balance or detect every possible text overlap. Inspect the full rendered page before merging. Changes to fonts/layout should be deliberate; update the PDF rather than bypassing the freshness check.

The workflow has read-only repository permissions and does not publish or modify files. A failing check is informational unless repository branch rules require it before merging.

## Website relationship

The website fetches `https://raw.githubusercontent.com/smbock42/resume/main/resume.pdf` at request time for its preview and download. Merge both the source and rebuilt PDF into main, then refresh the website to see the updated document; no website build or release is needed. These checks ensure the committed PDF matches its source.
