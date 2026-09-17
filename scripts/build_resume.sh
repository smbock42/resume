#!/usr/bin/env bash
set -euo pipefail
mkdir -p build
"${TECTONIC:-tectonic}" --untrusted --keep-logs \
  --bundle https://relay.fullyjustified.net/default_bundle_v33.tar \
  --outdir build resume.tex
