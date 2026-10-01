.PHONY: help setup serve build clean typecheck validate validate-content validate-site verify webp avif imgdims

help:
	@echo "Available commands:"
	@echo "  setup       - git submodules + npm ci"
	@echo "  serve       - Hugo dev server (localhost:1313)"
	@echo "  build       - Production build (hugo --gc --minify)"
	@echo "  typecheck   - TypeScript --noEmit"
	@echo "  validate    - Validate post front-matter"
	@echo "  verify      - Run validation, typecheck, build, and generated-site checks"
	@echo "  webp/avif/imgdims - Refresh modern siblings and image dimensions"
	@echo "  clean       - Remove build artifacts"

setup:
	git submodule update --init --recursive
	npm ci

serve:
	hugo server --disableFastRender --navigateToChanged

build:
	hugo --gc --minify

typecheck:
	npm run typecheck

validate:
	python3 scripts/validate-frontmatter.py

validate-content:
	python3 scripts/validate-content-safety.py

validate-site:
	python3 scripts/validate-site-output.py

verify:
	npm run verify

webp avif imgdims:
	bash scripts/build-images.sh

clean:
	rm -rf public resources/_gen .hugo_build.lock
