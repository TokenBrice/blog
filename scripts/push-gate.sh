#!/usr/bin/env bash
# Local mirror of .github/workflows/hugo.yml's build job.

set -Eeuo pipefail

cd "$(dirname "$0")/.."

EXPECTED_HUGO_VERSION="${EXPECTED_HUGO_VERSION:-0.161.1}"
EXPECTED_NODE_MAJOR="${EXPECTED_NODE_MAJOR:-20}"

gate_tmp="$(mktemp -d)"
preexisting_static_untracked="$gate_tmp/preexisting-static-untracked"
git ls-files --others --exclude-standard -z -- static/img > "$preexisting_static_untracked"
image_dims_was_clean=0
resources_was_clean=0
[[ -z "$(git status --porcelain -- data/imageDims.json)" ]] && image_dims_was_clean=1
[[ -z "$(git status --porcelain -- resources/_gen)" ]] && resources_was_clean=1

cleanup() {
  local status=$?

  if [[ "${PUSH_GATE_KEEP_ARTIFACTS:-0}" != "1" ]]; then
    git ls-files --others --exclude-standard -z -- static/img | while IFS= read -r -d '' f; do
      case "$f" in
        *.avif|*.webp)
          if ! grep -zFxq -- "$f" "$preexisting_static_untracked"; then
            rm -f -- "$f"
          fi
          ;;
      esac
    done

    if [[ "$image_dims_was_clean" -eq 1 ]]; then
      git restore -- data/imageDims.json 2>/dev/null || true
    fi
    if [[ "$resources_was_clean" -eq 1 ]]; then
      git restore -- resources/_gen 2>/dev/null || true
    fi
  fi

  rm -rf "$gate_tmp"
  exit "$status"
}
trap cleanup EXIT

step() {
  printf '\n==> %s\n' "$1"
}

die() {
  printf 'push-gate: %s\n' "$1" >&2
  exit 1
}

require_cmd() {
  local cmd="$1"
  local install_hint="${2:-}"

  if ! command -v "$cmd" >/dev/null 2>&1; then
    if [[ -n "$install_hint" ]]; then
      die "required command '$cmd' is missing. $install_hint"
    fi
    die "required command '$cmd' is missing"
  fi
}

verify_hugo_version() {
  require_cmd hugo "Install Hugo Extended $EXPECTED_HUGO_VERSION."

  local version
  version="$(hugo version)"
  if [[ "$version" != *"v${EXPECTED_HUGO_VERSION}"* ]]; then
    die "expected Hugo $EXPECTED_HUGO_VERSION, got: $version"
  fi
  if [[ "$version" != *"+extended"* ]]; then
    die "expected Hugo Extended, got: $version"
  fi
  printf '%s\n' "$version"
}

verify_node_version() {
  require_cmd node "Install Node.js $EXPECTED_NODE_MAJOR to match GitHub Actions."
  require_cmd npm "Install npm."

  local node_version node_major
  node_version="$(node --version)"
  node_major="${node_version#v}"
  node_major="${node_major%%.*}"

  if [[ "$node_major" != "$EXPECTED_NODE_MAJOR" ]]; then
    printf 'push-gate: warning: GitHub Actions uses Node.js %s, local node is %s\n' \
      "$EXPECTED_NODE_MAJOR" "$node_version" >&2
  else
    printf '%s\n' "$node_version"
  fi
}

verify_submodule_remote_refs() {
  if [[ ! -f .gitmodules ]]; then
    printf 'No .gitmodules file; skipping submodule checkout verification.\n'
    return
  fi

  local found=0
  while read -r key path; do
    found=1

    local name url sha submodule_tmp safe_name
    name="${key#submodule.}"
    name="${name%.path}"
    url="$(git config --file .gitmodules --get "submodule.${name}.url")"
    if git -C "$path" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      sha="$(git -C "$path" rev-parse HEAD)"
    else
      sha=""
    fi

    if [[ -z "$sha" ]]; then
      sha="$(git ls-files -s -- "$path" | awk '{print $2}' || true)"
    fi
    if [[ -z "$sha" ]]; then
      die "could not resolve gitlink SHA for submodule '$path'"
    fi

    printf 'Checking %s at %s from %s\n' "$path" "$sha" "$url"
    safe_name="${name//[^[:alnum:]_.-]/_}"
    submodule_tmp="$gate_tmp/submodule-${safe_name}"
    mkdir -p "$submodule_tmp"
    git -C "$submodule_tmp" init -q
    git -C "$submodule_tmp" remote add origin "$url"
    if ! GIT_TERMINAL_PROMPT=0 git -C "$submodule_tmp" -c protocol.version=2 \
      fetch --no-tags --depth=1 origin "$sha"; then
      die "GitHub Actions cannot fetch submodule '$path' at $sha from $url"
    fi
  done < <(git config --file .gitmodules --get-regexp '^submodule\..*\.path$' || true)

  if [[ "$found" -eq 0 ]]; then
    printf 'No submodules configured; skipping submodule checkout verification.\n'
  fi
}

ensure_submodules_initialized() {
  if [[ ! -f .gitmodules ]]; then
    return
  fi

  local missing=0
  while read -r _ path; do
    if ! git -C "$path" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      missing=1
    fi
  done < <(git config --file .gitmodules --get-regexp '^submodule\..*\.path$' || true)

  if [[ "$missing" -eq 1 ]]; then
    git submodule update --init --recursive
  fi
}

generate_missing_webp() {
  require_cmd cwebp "Install WebP tools, for example: sudo apt-get install webp"

  while IFS= read -r -d '' src; do
    local webp="${src%.*}.webp"
    if [[ ! -f "$webp" ]]; then
      printf 'Generating %s\n' "$webp"
      cwebp -quiet -q 80 "$src" -o "$webp"
    fi
  done < <(find static/img -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \) -print0)
}

generate_missing_avif() {
  require_cmd avifenc "Install libavif tools, for example: sudo apt-get install libavif-bin"

  local failed=0
  while IFS= read -r -d '' src; do
    local avif="${src%.*}.avif"
    if [[ ! -f "$avif" ]]; then
      if ! avifenc -q 52 --speed 6 "$src" "$avif" >/dev/null; then
        printf 'AVIF generation failed: %s\n' "$src" >&2
        failed=1
      fi
    fi
  done < <(find static/img -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \) -print0)

  return "$failed"
}

step "Checkout"
verify_submodule_remote_refs
ensure_submodules_initialized

step "Setup Hugo"
verify_hugo_version

step "Install Dart Sass"
if command -v sass >/dev/null 2>&1; then
  sass --version
else
  printf 'push-gate: warning: sass command not found; GitHub Actions installs Dart Sass before building.\n' >&2
fi

step "Setup Node.js"
verify_node_version

step "Install Node.js dependencies"
npm ci

step "Validate post front-matter"
npm run validate:frontmatter

step "Validate content safety"
npm run validate:content

step "TypeScript typecheck"
npm run typecheck

step "Generate missing WebP images"
generate_missing_webp

step "Generate missing AVIF siblings"
generate_missing_avif

step "Verify ImageMagick and jq installed"
require_cmd identify "Install ImageMagick, for example: sudo apt-get install imagemagick"
require_cmd jq "Install jq, for example: sudo apt-get install jq"

step "Generate image dimensions manifest"
bash scripts/gen-img-dims.sh

step "Build with Hugo"
if [[ -d public ]] && ! rm -rf public 2>/dev/null; then
  sleep 1
  rm -rf public
fi
HUGO_CACHEDIR="$gate_tmp/hugo_cache" HUGO_ENV=production HUGO_ENVIRONMENT=production \
  hugo --gc --minify --environment production

step "Validate generated site output"
npm run validate:site

step "Upload artifact"
test -d public || die "Hugo did not produce ./public"
printf 'OK: local push gate matched the GitHub Pages build job through artifact creation.\n'
