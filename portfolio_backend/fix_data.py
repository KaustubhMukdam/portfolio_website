#!/usr/bin/env python3
"""
One-off data fixer: updates existing Skill.icon_class values to valid
Font Awesome 6 classes so icons render on the frontend.

Run:
  cd portfolio_backend
  venv\Scripts\activate   # on Windows
  python fix_data.py
"""

from app import create_app
from app.models import db, Skill

ICON_MAP = {
    'Python': 'fab fa-python',
    'Flask': 'fas fa-flask',
    'HTML/CSS': 'fab fa-html5',
    'Git': 'fab fa-git-alt',
    'MySQL': 'fas fa-database',
    'PostgreSQL': 'fas fa-database',
    'Machine Learning': 'fas fa-brain',
}

def main():
    app = create_app()
    with app.app_context():
        updated = 0
        for name, icon in ICON_MAP.items():
            skill = Skill.query.filter_by(name=name).first()
            if skill and skill.icon_class != icon:
                skill.icon_class = icon
                updated += 1
        if updated:
            db.session.commit()
        print(f"✅ Updated {updated} skill icon(s). If 0, data already correct.")

if __name__ == '__main__':
    main()


