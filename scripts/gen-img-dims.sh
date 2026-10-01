#!/usr/bin/env bash
# Scan image headers once; serialize the compatible /img/path -> {w,h} map once.
# Requires python3 and ImageMagick identify. AVIF is included; GIF uses frame zero.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - <<'PY'
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

if not shutil.which('identify'):
    raise SystemExit("gen-img-dims.sh: ImageMagick 'identify' not found in PATH")
files = sorted(p for p in Path('static/img').rglob('*')
               if p.is_file() and p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp', '.avif', '.gif'})
# One process for the entire inventory. Output contains no filenames, so spaces,
# quotes and Unicode in paths cannot corrupt the JSON or the dimension parsing.
result = subprocess.run(['identify', '-ping', '-format', '%w %h\n',
                         *[str(p) + '[0]' for p in files]],
                        check=True, text=True, capture_output=True) if files else None
rows = result.stdout.splitlines() if result else []
if len(rows) != len(files):
    raise SystemExit('gen-img-dims.sh: identify returned an incomplete dimension inventory')
dimensions = {}
for path, row in zip(files, rows):
    width, height = map(int, row.split())
    if width <= 0 or height <= 0:
        raise SystemExit(f'gen-img-dims.sh: invalid dimensions for {path}')
    dimensions['/' + path.relative_to('static').as_posix()] = {'w': width, 'h': height}
output = Path('data/imageDims.json')
output.parent.mkdir(exist_ok=True)
content = json.dumps(dimensions, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
if not output.exists() or output.read_text() != content:
    with tempfile.NamedTemporaryFile('w', dir=output.parent, encoding='utf-8', delete=False) as temp:
        temp.write(content)
        name = temp.name
    os.replace(name, output)
    status = 'wrote'
else:
    status = 'unchanged'
print(f'gen-img-dims.sh: {status} {output} ({len(dimensions)} entries)')
PY
