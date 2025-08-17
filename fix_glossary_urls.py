#!/usr/bin/env python3

import json
import re

def fix_glossary_urls():
    """Remove /p/ prefixes from glossary article URLs"""
    
    # Load the glossary
    with open('data/glossary.json', 'r', encoding='utf-8') as f:
        glossary = json.load(f)
    
    fixed_count = 0
    
    # Process each term
    for term in glossary['en']['terms']:
        if 'related_articles' in term:
            for article in term['related_articles']:
                if 'url' in article and article['url'].startswith('/p/'):
                    # Remove the /p/ prefix
                    article['url'] = article['url'].replace('/p/', '/', 1)
                    fixed_count += 1
    
    # Save the updated glossary
    with open('data/glossary.json', 'w', encoding='utf-8') as f:
        json.dump(glossary, f, indent=2, ensure_ascii=False)
    
    print(f"Fixed {fixed_count} URLs by removing /p/ prefixes")

if __name__ == "__main__":
    fix_glossary_urls()
