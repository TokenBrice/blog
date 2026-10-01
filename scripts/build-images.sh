#!/usr/bin/env bash
# No arguments. Committed data/imageHashes.json records the master bytes used
# for siblings. Bootstrap existing siblings by recording their current masters
# once; thereafter a new/changed master or missing sibling requires encoding.
# Encoder settings are part of the manifest, so changing them invalidates it.
# Requires python3, cwebp and avifenc when an image needs generation, plus identify
# for the final batched dimension pass. Outputs replace siblings atomically.
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ $# -ne 0 ]]; then
  echo "build-images.sh: accepts no arguments" >&2
  exit 1
fi
python3 - <<'PY'
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

manifest_path = Path('data/imageHashes.json')
settings = {'webp': 'cwebp -q 80', 'avif': 'avifenc -q 52 --speed 6'}
manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
previous = manifest.get('masters', {}) if manifest.get('settings') == settings else {}
masters = sorted(p for p in Path('static/img').rglob('*')
                 if p.is_file() and p.suffix.lower() in {'.png', '.jpg', '.jpeg'})
# Two legacy stems have both PNG and JPEG masters. Their shared sibling is
# generated from PNG (then JPG, then JPEG), never whichever file is visited last.
# A change to any source in the group refreshes its shared siblings once.
groups = {}
hashes = {}
for master in masters:
    groups.setdefault(master.with_suffix(''), []).append(master)
    key = '/' + master.relative_to('static').as_posix()
    hashes[key] = hashlib.sha256(master.read_bytes()).hexdigest()
generated = 0
preference = {'.png': 0, '.jpg': 1, '.jpeg': 2}
for group in groups.values():
    master = min(group, key=lambda p: (preference[p.suffix.lower()], str(p)))
    stale = any(previous.get('/' + p.relative_to('static').as_posix()) !=
                hashes['/' + p.relative_to('static').as_posix()] for p in group)
    for extension, encoder, arguments in [('.webp', 'cwebp', ['-q', '80']),
                                          ('.avif', 'avifenc', ['-q', '52', '--speed', '6'])]:
        sibling = master.with_suffix(extension)
        if not stale and sibling.exists():
            continue
        if not shutil.which(encoder):
            raise SystemExit(f'build-images.sh: {encoder} not found in PATH')
        fd, temporary = tempfile.mkstemp(prefix='.tb-image-', suffix=extension, dir=master.parent)
        os.close(fd)
        try:
            if encoder == 'cwebp':
                command = [encoder, *arguments, str(master), '-o', temporary]
            else:
                command = [encoder, *arguments, str(master), temporary]
            subprocess.run(command, check=True)
            if Path(temporary).stat().st_size == 0:
                raise RuntimeError(f'{encoder} produced an empty image for {master}')
            os.replace(temporary, sibling)
            generated += 1
        finally:
            Path(temporary).unlink(missing_ok=True)
output = {'settings': settings, 'masters': hashes}
content = json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
manifest_path.parent.mkdir(exist_ok=True)
if not manifest_path.exists() or manifest_path.read_text() != content:
    with tempfile.NamedTemporaryFile('w', dir=manifest_path.parent, encoding='utf-8', delete=False) as temp:
        temp.write(content)
        name = temp.name
    os.replace(name, manifest_path)
print(f'build-images.sh: {len(masters)} masters, {generated} siblings regenerated')
PY
bash scripts/gen-img-dims.sh
