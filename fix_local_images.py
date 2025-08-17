#!/usr/bin/env python3

import json
import os
import glob
import re
from pathlib import Path

def find_broken_image_references():
    """
    Comprehensive diagnosis of image path issues
    """
    issues = []
    
    # 1. Check if static images exist
    static_dir = Path("static")
    if static_dir.exists():
        image_files = []
        for pattern in ["**/*.jpg", "**/*.jpeg", "**/*.png", "**/*.gif", "**/*.svg", "**/*.webp"]:
            image_files.extend(static_dir.glob(pattern))
        print(f"Found {len(image_files)} image files in static directory")
        
        # Sample some image paths
        for img in image_files[:10]:
            relative_path = str(img.relative_to("static"))
            print(f"  Sample: /{relative_path}")
    else:
        issues.append("No static directory found")
    
    # 2. Check frontmatter image references
    content_dir = Path("content")
    if content_dir.exists():
        md_files = list(content_dir.glob("**/*.md"))
        frontmatter_images = []
        
        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Look for frontmatter image references
                    if content.startswith('---'):
                        frontmatter_end = content.find('---', 3)
                        if frontmatter_end != -1:
                            frontmatter = content[3:frontmatter_end]
                            
                            # Find image lines
                            for line in frontmatter.split('\n'):
                                if 'image:' in line and '/img/' in line:
                                    image_path = line.split('image:')[1].strip()
                                    frontmatter_images.append((str(md_file), image_path))
            except Exception as e:
                issues.append(f"Error reading {md_file}: {e}")
        
        print(f"Found {len(frontmatter_images)} frontmatter image references")
        for file, img_path in frontmatter_images[:5]:
            print(f"  Sample: {img_path} in {file}")
    
    # 3. Check content image references
    content_images = []
    if content_dir.exists():
        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Find markdown image references
                    img_patterns = [
                        r'!\[.*?\]\((/img/[^)]+)\)',  # ![alt](/img/path)
                        r'{{<\s*figure\s+src="(/img/[^"]+)"',  # Hugo shortcode
                        r'src="(/img/[^"]+)"',  # HTML src
                    ]
                    
                    for pattern in img_patterns:
                        matches = re.findall(pattern, content)
                        for match in matches:
                            content_images.append((str(md_file), match))
                            
            except Exception as e:
                issues.append(f"Error reading content from {md_file}: {e}")
    
    print(f"Found {len(content_images)} content image references")
    for file, img_path in content_images[:10]:
        print(f"  Sample: {img_path} in {file}")
    
    # 4. Verify image paths exist
    missing_images = []
    all_referenced_images = [img for _, img in frontmatter_images + content_images]
    
    for img_path in set(all_referenced_images):
        if img_path.startswith('/img/'):
            static_path = Path("static") / img_path[1:]  # Remove leading /
            if not static_path.exists():
                missing_images.append(img_path)
    
    if missing_images:
        print(f"WARNING: {len(missing_images)} referenced images not found:")
        for img in missing_images[:10]:
            print(f"  Missing: {img}")
    else:
        print("✓ All referenced images exist in static directory")
    
    return issues

def clean_hugo_cache():
    """
    Clean Hugo's cache and public directories
    """
    print("\\nCleaning Hugo cache and build artifacts...")
    
    # Remove common Hugo cache/build directories
    dirs_to_clean = ['public', 'resources/_gen', '.hugo_build.lock']
    
    for dir_path in dirs_to_clean:
        if os.path.exists(dir_path):
            if os.path.isdir(dir_path):
                import shutil
                shutil.rmtree(dir_path)
                print(f"  Removed directory: {dir_path}")
            else:
                os.remove(dir_path)
                print(f"  Removed file: {dir_path}")
        else:
            print(f"  Not found: {dir_path}")

def check_hugo_config():
    """
    Verify Hugo configuration for local development
    """
    print("\\nChecking Hugo configuration...")
    
    config_files = ['hugo.yaml', 'hugo.yml', 'hugo.toml', 'config.yaml', 'config.yml', 'config.toml']
    
    for config_file in config_files:
        if os.path.exists(config_file):
            print(f"  Found config: {config_file}")
            
            if config_file.endswith(('.yaml', '.yml')):
                try:
                    import yaml
                    with open(config_file, 'r') as f:
                        config = yaml.safe_load(f)
                        
                    print(f"    baseURL: {config.get('baseurl', 'not set')}")
                    print(f"    static dirs: looking for images in /static/")
                    
                    # Check if relativeURLs or canonifyURLs might affect local development
                    if 'params' in config:
                        params = config['params']
                        print(f"    image processing enabled: {params.get('imageProcessing', {}).get('cover', {}).get('enabled', 'not set')}")
                        
                except Exception as e:
                    print(f"    Error reading YAML config: {e}")
            
            break
    else:
        print("  No Hugo config file found!")

def main():
    """
    Run comprehensive image path diagnosis and fixes
    """
    print("🔍 TokenBrice Blog - Image Path Diagnosis & Fix")
    print("=" * 50)
    
    # Check current working directory
    cwd = os.getcwd()
    print(f"Working directory: {cwd}")
    
    if not os.path.exists('hugo.yaml') and not os.path.exists('config.yaml'):
        print("ERROR: No Hugo config found. Are you in the right directory?")
        return
    
    # 1. Diagnose image references
    print("\\n1. Diagnosing image references...")
    issues = find_broken_image_references()
    
    # 2. Check Hugo configuration
    check_hugo_config()
    
    # 3. Clean cache
    clean_hugo_cache()
    
    # 4. Final recommendations
    print("\\n" + "=" * 50)
    print("🔧 RECOMMENDATIONS FOR LOCAL DEVELOPMENT:")
    print("=" * 50)
    
    if issues:
        print("❌ Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✅ No critical issues detected")
    
    print("\\n📝 To test images locally:")
    print("  1. Run: hugo server --bind 0.0.0.0 --port 1313")
    print("  2. Visit: http://localhost:1313")
    print("  3. Images should be served from: http://localhost:1313/img/...")
    
    print("\\n🔄 If images are still broken:")
    print("  1. Hard refresh your browser (Ctrl+F5 or Cmd+Shift+R)")
    print("  2. Clear browser cache for localhost:1313")
    print("  3. Check browser console for 404 errors on specific images")
    print("  4. Verify the image files exist in /static/img/")

if __name__ == "__main__":
    main()
