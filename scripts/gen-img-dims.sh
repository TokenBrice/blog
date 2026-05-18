#!/usr/bin/env bash
# gen-img-dims.sh — build-time image dimension manifest for CLS-free static covers.
#
# Walks static/img/ and emits data/imageDims.json mapping each /img/<path> to
# {"w":<width>,"h":<height>}. Hugo templates consume this to set width/height
# on <img> tags whose src is a static path (i.e. not a page-bundle Resource).
#
# Dependencies:
#   - ImageMagick `identify` (pacman -S imagemagick / apt-get install imagemagick)
#   - jq (for safe JSON assembly, handles filenames containing quotes/backslashes)
# Re-run whenever images are added to static/img/. Zone J wires this into CI
# before `hugo build`.

set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v identify >/dev/null 2>&1; then
  echo "gen-img-dims.sh: ImageMagick 'identify' not found in PATH" >&2
  exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
  echo "gen-img-dims.sh: 'jq' not found in PATH" >&2
  exit 1
fi

out=data/imageDims.json
mkdir -p data

tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT

# Build the manifest by feeding (path, width, height) triples into jq.
# Each value is on its own line; jq is invoked once per image so the path
# bytes never have to round-trip through any string-encoding logic in bash.
echo '{}' > "$tmp"
while IFS= read -r -d '' f; do
  dim=$(identify -format '%w %h' "${f}[0]" 2>/dev/null || echo "")
  [[ -z "$dim" ]] && continue
  w=${dim% *}
  h=${dim##* }
  rel="/${f#static/}"
  jq --arg k "$rel" --argjson w "$w" --argjson h "$h" \
     '. + {($k): {w: $w, h: $h}}' "$tmp" > "$tmp.new"
  mv "$tmp.new" "$tmp"
done < <(find static/img -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.webp' -o -iname '*.gif' \) -print0 | sort -z)

mv "$tmp" "$out"
trap - EXIT

count=$(jq 'length' "$out")
echo "gen-img-dims.sh: wrote $out ($count entries)"
