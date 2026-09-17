# Status

## Updated
2026-09-17 — Typography/date consistency pass and grouped Lockheed roles prepared.

## Objective
Maintain a polished one-page engineering resume with accurate ownership, clear hierarchy, and dependable PDF validation.

## Decisions
Bold upright employers share the main left edge; role lines are regular text. Named projects indent 14pt and their hollow-circle explanation bullets indent 28pt. Direct job accomplishments use solid black bullets at 14pt. All dates, including education, use regular 11pt text with aligned right edges and three-letter month abbreviations. Dates belong to individual roles. Lockheed appears once with two separately dated roles; no continuous employment range is implied. Education follows Experience; confirmed honor is styled Cum Laude in upright text. Keep Projects heading and one Homelab entry for now.

Keep approved career content: custom Envoy/control-plane implementation, configurable deployment targets/strategies/component versions, build-once delivery, and approximate 25–30 minute release duration. Do not imply ownership of the whole platform. Restricted work stays generic, with no project name, purpose, geography or compliance context. Degree type remains unspecified; Computer Science graduation in 2025 and Cum Laude are confirmed.

## Current state
resume.tex and rebuilt resume.pdf contain the consistency pass. PR compilation/layout/freshness validation is active on main. Website fetches main/resume.pdf at runtime; no website rebuild needed, though GitHub raw propagation can take a few minutes. Earlier flat-hierarchy and bold-date choices are superseded by these decisions.

## Verification
Pinned Tectonic compilation and PDF checks pass: one Letter page, searchable text, margins/font sizes and rebuilt PDF parity. Final full-page render visually inspected for hierarchy, spacing, wrapping and typography. All six date lines have identical regular font/size and right edges within 0.1pt. Lockheed company heading occurs once; both roles retain original dates. No career accomplishments changed.

## Next steps
Finish PR validation and merge. User may provide additional projects and sanitized work-summary evidence later.
