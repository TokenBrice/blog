#!/usr/bin/env bash
# Run Lighthouse audits against the local Hugo site.
# Usage: ./lighthouse.sh [page1 page2 ...]
# Defaults to "/" if no pages specified.
# Reports are saved in lighthouse-reports/

set -euo pipefail

PORT=1314
REPORT_DIR="$(cd "$(dirname "$0")" && pwd)/lighthouse-reports"
HUGO_PID=""

cleanup() {
  if [ -n "$HUGO_PID" ]; then
    kill "$HUGO_PID" 2>/dev/null || true
    wait "$HUGO_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT

# Default pages to test
PAGES=("${@:-/}")

mkdir -p "$REPORT_DIR"

# Start Hugo server
echo "Starting Hugo server on port $PORT..."
hugo server --port "$PORT" --disableLiveReload --baseURL "http://localhost:$PORT" --environment production --minify &>/dev/null &
HUGO_PID=$!

# Wait for server to be ready
for i in $(seq 1 10); do
  if curl -s -o /dev/null -w "" "http://localhost:$PORT/"; then
    break
  fi
  sleep 1
done

TIMESTAMP=$(date +%Y%m%d-%H%M%S)

for PAGE in "${PAGES[@]}"; do
  SLUG=$(echo "$PAGE" | sed 's|^/||; s|/$||; s|/|_|g')
  [ -z "$SLUG" ] && SLUG="homepage"

  echo "Running Lighthouse on $PAGE -> $SLUG..."
  npx lighthouse "http://localhost:$PORT$PAGE" \
    --chrome-flags="--headless --no-sandbox" \
    --preset desktop \
    --output html \
    --output-path "$REPORT_DIR/${SLUG}_${TIMESTAMP}.report.html" \
    --quiet 2>&1

  # Also generate JSON
  npx lighthouse "http://localhost:$PORT$PAGE" \
    --chrome-flags="--headless --no-sandbox" \
    --preset desktop \
    --output json \
    --output-path "$REPORT_DIR/${SLUG}_${TIMESTAMP}.report.json" \
    --quiet 2>&1
done

echo ""
echo "Reports saved in $REPORT_DIR/"
ls -lh "$REPORT_DIR"/*"$TIMESTAMP"* 2>/dev/null
