.PHONY: help setup dev build serve clean deploy lint format

# Default target
help:
	@echo "Available commands:"
	@echo "  setup     - Initial project setup (submodules + dependencies)"
	@echo "  dev       - Start development mode (webpack watch + hugo server)"
	@echo "  build     - Build production site"
	@echo "  serve     - Start Hugo development server"
	@echo "  clean     - Clean build artifacts"
	@echo "  lint      - Lint JavaScript/Vue files"
	@echo "  format    - Format code with Prettier"

# Initial setup
setup:
	git config --global --add safe.directory /workspace || true
	git submodule update --init --recursive
	yarn install

# Development mode
dev:
	@echo "Starting development mode..."
	@echo "Run 'make serve' in another terminal for Hugo server"
	yarn dev

# Build production site
build:
	yarn install
	yarn build:production
	hugo --gc --minify
	yarn optimize

# Start Hugo server
serve:
	hugo server --disableFastRender --navigateToChanged

# Clean build artifacts
clean:
	rm -rf public/*
	rm -f static/js/main.js
	rm -f .hugo_build.lock

# Lint code
lint:
	yarn lint

# Format code
format:
	yarn format

# Docker development
docker-dev:
	docker-compose up -d --build

# Docker stop
docker-stop:
	docker-compose down
