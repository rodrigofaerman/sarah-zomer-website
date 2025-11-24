import json
import re
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BRANDING_FILE = os.path.join(BASE_DIR, 'DNA', 'branding.json')
CSS_FILE = os.path.join(BASE_DIR, 'style.css')
HTML_FILE = os.path.join(BASE_DIR, 'index.html')

def load_branding():
    try:
        with open(BRANDING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading branding.json: {e}")
        return None

def update_css(branding):
    if not branding or 'colors' not in branding or 'fonts' not in branding:
        return

    try:
        with open(CSS_FILE, 'r', encoding='utf-8') as f:
            css_content = f.read()

        # Update Colors
        for key, value in branding['colors'].items():
            # Regex to find --color-{key}: ...;
            # Handle underscore to hyphen conversion
            css_key = key.replace('_', '-')
            pattern = fr'(--color-{css_key}:\s*)([^;]+)(;)'
            if re.search(pattern, css_content):
                css_content = re.sub(pattern, fr'\1{value}\3', css_content)
            else:
                print(f"Warning: CSS variable --color-{css_key} not found.")

        # Update Fonts
        for key, value in branding['fonts'].items():
             css_key = key.replace('_', '-')
             pattern = fr'(--font-{css_key}:\s*)([^;]+)(;)'
             if re.search(pattern, css_content):
                css_content = re.sub(pattern, fr'\1{value}\3', css_content)

        with open(CSS_FILE, 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        print("CSS updated successfully.")

    except Exception as e:
        print(f"Error updating CSS: {e}")

def update_html(branding):
    if not branding or 'content' not in branding:
        return

    try:
        with open(HTML_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Update Content by ID
        # We look for id="key" ... >Content<
        # This is a simple regex approach. 
        
        for key, value in branding['content'].items():
            # Regex to find element with id="{key}" and replace its content
            # Matches: <tag ... id="key" ... > OLD CONTENT </tag>
            # We assume the tag doesn't have nested tags that match the closing tag pattern simply.
            # For robustness with simple text/span replacements:
            
            # Pattern: (<[^>]+id=["']key["'][^>]*>)(.*?)(</[^>]+>)
            # We need to be careful with "key" being hero-title (hyphenated) vs hero_title (underscore in json)
            html_id = key.replace('_', '-')
            
            pattern = re.compile(fr'(<[^>]+id=["\']{html_id}["\'][^>]*>)(.*?)(</[^>]+>)', re.DOTALL)
            
            if pattern.search(html_content):
                html_content = pattern.sub(fr'\1{value}\3', html_content)
            else:
                print(f"Warning: HTML element with id='{html_id}' not found.")

        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print("HTML updated successfully.")

    except Exception as e:
        print(f"Error updating HTML: {e}")

def main():
    print("Starting website update...")
    branding = load_branding()
    if branding:
        update_css(branding)
        update_html(branding)
        print("Website update complete.")
    else:
        print("Failed to load branding.")

if __name__ == "__main__":
    main()
