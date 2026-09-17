# Status

## Updated
2026-09-17 — Project heading left alignment corrected; date readability and cum laude retained.

## Objective
Present professional experience clearly for an engineering referral, with accurate ownership and project context.

## Decisions
Employers and roles share the main left edge. Company names are bold upright text, never italic. Named projects indent 14pt under their employer; their explanations indent 28pt. Roles without named projects have direct bullets at 14pt. This supersedes prior flat-heading alignment changes. Preserve one page, readable bold dates, confirmed cum laude, current content and Projects heading. Restricted work remains generic without its name, purpose, geography or compliance context.

## Current state
PR #1 merged as 61dd3cf; validation is active on main: pinned Tectonic 0.17.0/v33 bundle and PyMuPDF, compile/layout/freshness checks, and uploaded PDF/PNG/log artifacts. Workflow runs read-only on PRs/main/manual dispatch. Website v0.5.0 independently adds runtime fetching of main/resume.pdf; no branch-rule changes are included.

resume.tex and resume.pdf include the experience-first hierarchy and separate neutral observability entry. Template now uses consistent margins, bold role headings, italic employer lines beneath, right-aligned dates, indented project subheadings and hanging open-circle bullets. Education is Cal Poly San Luis Obispo, Computer Science, 2025; user has not specified the formal degree type. Cum laude confirmed by the user and added beside Computer Science. Contact email is the user-confirmed personal-domain address. Older roles are condensed, keeping Lockheed full-stack ownership, ML research and SOC automation impact. General Kubernetes maintenance was omitted to keep project attribution clear.

Lockheed software internship end June 2025 was cross-checked with LinkedIn; other role dates remain as previously verified. Compile with Tectonic 0.17.0: `tectonic resume.tex`.

## Verification
Latest hierarchy repair: pinned compilation and PDF layout/freshness checks pass. Full one-page render inspected: every employer returns to main left edge, named Apple projects nest beneath it and explanations nest one further level. Company italics removed; no content claims changed. Older alignment notes below are historical and superseded.
User clarified horizontal indentation, not vertical spacing. Removed extra project-heading indent (23pt → 10pt) and restored original 3pt vertical spacing. Measured role and three Apple project headings at x=53.163pt; one-page PDF checks and visual inspection pass. Previous vertical-spacing interpretation below is superseded.
Latest refinement: compared older LaTeX history and measured heading coordinates; horizontal project alignment was consistent. Removed the first project’s extra 3pt leading gap, enlarged experience dates to 11pt bold, retained other layout. Pinned compilation/PDF checks pass, one Letter page; final full-page render inspected.
Latest formatting correction merged as b17497d via PR #2. Hosted run 35196539074 passed. PDF is 29585 bytes, one Letter page, with 10pt body text. Full rendered page visually inspected after final Projects rename; earlier hash below is historical. User explicitly preferred the supplied older formatting over the previous flat hierarchy.
Current PDF is one page, 23047 bytes, SHA-256 44828a73a11c098332ebd30615f76c2926cffc367639964a08560d48682d750d. Public website delivered these bytes and rendered the new ordering after GitHub raw propagation, without a website rebuild. Independent visual review found no overlap or clipping.
Nine validation regression fixtures pass, including intentional failures for stale PDF content, changed link targets, margin overflow, undersized text, wrong paper and an extra page. The real current resume recompiles and passes all checks without changing its committed PDF. GitHub PR #1 run 35191938177 passed on a clean hosted runner in 28 seconds, including compilation/freshness checks and review-artifact upload. PR #1 is merged. Final PR run 35193208896 and main run 35193347885 passed; branch protection remains unchanged.

Tectonic compilation succeeded without layout warnings. PDF remains one page with education following experience, both Apple project headings and configurable CI/CD details present. Final rendered page visually inspected for hierarchy, wrapping, margins and readability. Email link verified. Git diff whitespace check passed.

## Next steps
The user approved proceeding with resume, LinkedIn and website updates. Work-laptop summary may later supply stronger verified technical detail and metrics.
