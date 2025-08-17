# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a multilingual (English/French) Hugo-based blog focused on DeFi content, with privacy-respecting analytics via Matomo. The site includes a custom Vue.js-powered media filtering system and is designed to be hosted on IPFS while maintaining full privacy compliance.

## Development Commands

### Building and Running

```bash
# Quick setup (recommended)
make setup                   # Initialize submodules and install dependencies

# Development workflow
make dev                     # Start webpack watch mode (in one terminal)
make serve                   # Start Hugo server (in another terminal)

# Alternative: traditional commands
yarn install                 # Install Node dependencies
yarn dev                     # Build Vue.js components with watch mode
hugo server                  # Start development server at http://localhost:1313

# Production build
make build                   # Complete production build
# OR step by step:
yarn build:production        # Build Vue.js components for production
hugo --gc --minify           # Generate optimized Hugo site
yarn optimize                # Optimize images in public/img

# Docker development (alternative)
make docker-dev              # Run via Docker at http://localhost:1313
```

### Initial Setup

```bash
# Quick setup
make setup

# Manual setup
git config --global --add safe.directory /workspace
git submodule update --init --recursive
yarn install
```

### Testing and Optimization

```bash
yarn run optimize          # Optimize images using Sharp
hugo --gc --minify         # Build with garbage collection and minification
```

## Architecture Overview

### Core Technologies
- **Hugo**: Static site generator with Stack theme
- **Vue.js 2**: Interactive filtering system for media content
- **Webpack**: Module bundling for Vue components
- **Sharp**: Image optimization
- **Docker**: Containerized development environment

### Directory Structure
- `content/`: Multilingual Hugo content (EN/FR)
- `src/js/`: Vue.js application source
  - `App.vue`: Main filtering component for media
  - `main.js`: Vue application entry point
  - `matomo-tracking.js`: Privacy-compliant analytics
- `data/`: JSON configuration files
  - `filters.json`: Multilingual filter definitions
  - `media.json`: Media content database
- `themes/`: Git submodules for Hugo themes
  - `hugo-theme-stack`: Main theme
  - `matomo`: Analytics integration
  - `hugo-notice`: Notice/alert components
- `build/`: Build configuration and optimization scripts
- `static/js/`: Compiled JavaScript output

### Key Components

#### Media Filtering System
The Vue.js application in `src/js/App.vue` provides dynamic filtering of media content based on:
- Tags (interview, discussion, meetup, commentary, mention)
- Language (French/English)
- Date ranges (automatically extracted from content)
- Media types (audio, video, post)

#### Multilingual Support
- Hugo's built-in i18n system
- Vue.js filters support both EN/FR with separate configurations
- Language-specific filter presets and naming

#### Privacy-First Design
- Matomo analytics with full IP anonymization
- CNIL compliance (French privacy authority)
- No cookie propagation
- IPFS hosting capability

### Build Process Flow

1. **Vue.js Compilation**: Webpack compiles Vue components from `src/js/` to `static/js/main.js`
2. **Hugo Generation**: Hugo processes content and themes, incorporating the compiled JS
3. **Image Optimization**: Sharp optimizes images in `public/img/` directory
4. **Theme Integration**: Three Hugo themes work together via theme composition

### Data Management

#### Adding New Filters
1. Update `data/filters.json` with new filter entries for both EN/FR
2. Add corresponding keys to `data/media.json` entries
3. Update Vue component's `selectedFilters` object in `App.vue`
4. Rebuild with `yarn run build`

#### Adding New Filter Categories
1. Define new category in `data/filters.json` with name, class, and values
2. Add category key to `selectedFilters` in `App.vue`
3. Add corresponding CSS class styling
4. Rebuild application

### Development Workflow

The codebase supports both Docker and local development. The Vue.js filtering system requires rebuilding when filter configurations change. Hugo's live reload works for content changes, but JavaScript changes require webpack recompilation.

### Theme Architecture

Uses Hugo's theme composition with three themes:
- `hugo-theme-stack`: Primary blog theme
- `matomo`: Analytics integration theme  
- `hugo-notice`: Alert/notice component theme

All themes are managed as Git submodules and must be initialized before building.
