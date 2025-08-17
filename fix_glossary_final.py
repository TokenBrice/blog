#!/usr/bin/env python3
"""
Fix glossary URLs to use relative paths and restore image functionality.
"""

import json
import yaml
from pathlib import Path

def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None
        
        end_marker = content.find('\n---\n', 4)
        if end_marker == -1:
            return None
        
        frontmatter_content = content[4:end_marker]
        return yaml.safe_load(frontmatter_content)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

def main():
    blog_root = Path('/home/ahirice/Documents/git/blog')
    
    # Load glossary
    with open(blog_root / 'data' / 'glossary.json', 'r', encoding='utf-8') as f:
        glossary = json.load(f)
    
    # Create a mapping of article titles to correct relative URLs
    content_dir = blog_root / 'content' / 'post'
    title_to_url = {}
    
    print("🔍 Building title-to-URL mapping...")
    for md_file in content_dir.rglob('*.md'):
        if md_file.name.endswith('.fr.md'):
            continue
            
        frontmatter = extract_frontmatter(md_file)
        if frontmatter and frontmatter.get('title'):
            title = frontmatter['title']
            if 'url' in frontmatter and frontmatter['url']:
                # Use relative URL from frontmatter
                relative_url = f"/{frontmatter['url']}/"
            else:
                # Fallback: use Hugo permalink structure (/p/:slug/)
                slug = md_file.stem
                relative_url = f"/p/{slug}/"
            
            title_to_url[title] = relative_url
    
    print(f"📖 Found {len(title_to_url)} articles with URLs")
    
    # Update glossary URLs to use relative paths
    updated_count = 0
    for term in glossary['en']['terms']:
        if 'related_articles' in term:
            for article in term['related_articles']:
                title = article['title']
                if title in title_to_url:
                    old_url = article['url']
                    new_url = title_to_url[title]
                    if old_url != new_url:
                        article['url'] = new_url
                        updated_count += 1
                        print(f"✅ Updated {title}")
                        print(f"   Old: {old_url}")
                        print(f"   New: {new_url}")
    
    # Save updated glossary
    with open(blog_root / 'data' / 'glossary.json', 'w', encoding='utf-8') as f:
        json.dump(glossary, f, indent=2, ensure_ascii=False)
    
    print(f"\n🎉 Fixed {updated_count} article URLs to use relative paths!")
    print("Now the links should work locally and the images should be restored!")

if __name__ == '__main__':
    main()
