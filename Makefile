.PHONY: help setup serve build clean typecheck validate webp avif imgdims

help:
	@echo "Available commands:"
	@echo "  setup       - git submodules + npm install"
	@echo "  serve       - Hugo dev server (localhost:1313)"
	@echo "  build       - Production build (hugo --gc --minify)"
	@echo "  typecheck   - TypeScript --noEmit"
	@echo "  validate    - Validate post front-matter"
	@echo "  webp        - Generate missing WebP siblings under static/img/"
	@echo "  avif        - Generate missing AVIF siblings under static/img/"
	@echo "  imgdims     - Refresh data/imageDims.json"
	@echo "  clean       - Remove build artifacts"

setup:
	git submodule update --init --recursive
	npm install

serve:
	hugo server --disableFastRender --navigateToChanged

build:
	hugo --gc --minify

typecheck:
	npm run typecheck

validate:
	python3 scripts/validate-frontmatter.py

webp:
	@find static/img -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \) | while read src; do \
		out="$${src%.*}.webp"; \
		[ -f "$$out" ] || cwebp -q 80 "$$src" -o "$$out"; \
	done

avif:
	@find static/img -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \) -print0 | \
		while IFS= read -r -d '' f; do \
			out="$${f%.*}.avif"; \
			[ -f "$$out" ] || avifenc --min 25 --max 35 --speed 6 "$$f" "$$out" 2>/dev/null || true; \
		done

imgdims:
	bash scripts/gen-img-dims.sh

clean:
	rm -rf public resources/_gen .hugo_build.lock
