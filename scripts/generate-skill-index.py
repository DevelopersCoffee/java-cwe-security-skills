#!/usr/bin/env python3
"""
Generate CWE Skill Index
Scans all cwe-* folders and generates a catalog page for documentation.
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# CWE Categories mapping
CWE_CATEGORIES = {
    'injection': {
        'name': '💉 Injection',
        'cwes': [77, 78, 79, 89, 90, 91, 93, 94, 113, 643, 917]
    },
    'cryptography': {
        'name': '🔐 Cryptography',
        'cwes': [321, 326, 327, 328, 329, 330, 780]
    },
    'authentication': {
        'name': '🔑 Authentication & Credentials',
        'cwes': [259, 287, 306, 307, 347, 522, 613, 798]
    },
    'access_control': {
        'name': '🚪 Access Control',
        'cwes': [22, 284, 434, 552, 601, 693, 732]
    },
    'data_exposure': {
        'name': '📝 Data Exposure',
        'cwes': [200, 209, 311, 319, 359, 501, 532]
    },
    'resource_mgmt': {
        'name': '⚡ Resource Management',
        'cwes': [190, 191, 369, 400, 606, 776, 1333]
    },
    'concurrency': {
        'name': '🔄 Concurrency',
        'cwes': [362, 367, 377, 820, 833]
    },
    'web_security': {
        'name': '🌐 Web Security',
        'cwes': [295]
    }
}

def get_cwe_number(folder_name):
    """Extract CWE number from folder name like 'cwe-89-sql-injection'"""
    match = re.match(r'cwe-(\d+)', folder_name)
    return int(match.group(1)) if match else None

def parse_skill_frontmatter(skill_path):
    """Parse YAML frontmatter from SKILL.md"""
    try:
        with open(skill_path, 'r') as f:
            content = f.read()
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                return yaml.safe_load(parts[1])
    except Exception:
        pass
    return {}

def get_category_for_cwe(cwe_num):
    """Determine which category a CWE belongs to"""
    for cat_id, cat_info in CWE_CATEGORIES.items():
        if cwe_num in cat_info['cwes']:
            return cat_id
    return 'other'

def generate_skill_page(skill_folder, skill_path, output_dir):
    """Generate individual skill documentation page"""
    frontmatter = parse_skill_frontmatter(skill_path)
    with open(skill_path, 'r') as f:
        content = f.read()
    
    # Remove YAML frontmatter for the doc page
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    
    output_path = output_dir / f"{skill_folder}.md"
    with open(output_path, 'w') as f:
        f.write(content)
    
    return frontmatter

def main():
    repo_root = Path(__file__).parent.parent
    skills_output_dir = repo_root / 'docs' / 'skills'
    skills_output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all CWE skill folders
    skills = []
    for folder in sorted(repo_root.iterdir()):
        if folder.is_dir() and folder.name.startswith('cwe-'):
            skill_path = folder / 'SKILL.md'
            if skill_path.exists():
                cwe_num = get_cwe_number(folder.name)
                frontmatter = generate_skill_page(
                    folder.name, skill_path, skills_output_dir)
                skills.append({
                    'folder': folder.name,
                    'cwe': cwe_num,
                    'name': frontmatter.get('name', folder.name),
                    'description': frontmatter.get('description', ''),
                    'category': get_category_for_cwe(cwe_num)
                })
    
    # Group by category
    by_category = defaultdict(list)
    for skill in skills:
        by_category[skill['category']].append(skill)
    
    print(f"✅ Generated {len(skills)} skill pages in docs/skills/")
    print(f"📁 Categories: {len(by_category)}")

if __name__ == '__main__':
    main()

