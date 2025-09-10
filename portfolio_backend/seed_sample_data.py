#!/usr/bin/env python3
"""
Seed the database with sample data for the portfolio
"""

from app import create_app, db
from app.models import Project, Skill, Experience, BlogPost, Testimonial
from datetime import datetime, date
import json

def create_sample_data():
    app = create_app()
    
    with app.app_context():
        # Ensure tables exist but DO NOT drop existing data
        db.create_all()
        
        # Sample Skills
        skills_data = [
            {'name': 'Python', 'category': 'Programming', 'proficiency_level': 5, 'icon_class': 'fab fa-python'},
            {'name': 'Flask', 'category': 'Framework', 'proficiency_level': 4, 'icon_class': 'fas fa-flask'},
            {'name': 'HTML/CSS', 'category': 'Frontend', 'proficiency_level': 4, 'icon_class': 'fab fa-html5'},
            {'name': 'Git', 'category': 'Tool', 'proficiency_level': 4, 'icon_class': 'fab fa-git-alt'},
            {'name': 'MySQL', 'category': 'Database', 'proficiency_level': 4, 'icon_class': 'fas fa-database'},
            {'name': 'PostgreSQL', 'category': 'Database', 'proficiency_level': 3, 'icon_class': 'fas fa-database'},
            {'name': 'Machine Learning', 'category': 'AI', 'proficiency_level': 4, 'icon_class': 'fas fa-brain'},
        ]
        
        for skill_data in skills_data:
            exists = Skill.query.filter_by(name=skill_data['name']).first()
            if not exists:
                db.session.add(Skill(**skill_data))
        
        # Sample Projects
        projects_data = [
            {
                'title': 'Portfolio Website',
                'description': 'A modern, responsive portfolio website with dark theme and smooth animations.',
                'long_description': 'This portfolio website showcases my skills and projects with a beautiful dark theme. Built with vanilla HTML, CSS, and JavaScript, it features smooth animations, responsive design, and integration with a Flask backend API.',
                'technologies': json.dumps(['HTML', 'CSS', 'JavaScript', 'Flask', 'SQLAlchemy']),
                'github_url': 'https://github.com/KaustubhMukdam/portfolio_website',
                'live_demo_url': 'https://kaustubhmukdam.github.io/portfolio_website',
                'image_url': None,
                'featured': True
            },
            {
                'title': 'Morse Code Converter (GUI and Sound)',
                'description': 'Text to Morse Code Converter with Morse Code sound and interactive GUI',
                'long_description': 'Built a comprehensive Text to Morse code converter with the help of Python, Tkinter for GUI and WinSound for sound',
                'technologies': json.dumps(['Python', 'Tkinter', 'WinSound']),
                'github_url': 'https://github.com/KaustubhMukdam/morse-code-converter-gui',
                # 'live_demo_url': 'https://morse-code-converter-gui.herokuapp.com',
                'image_url': None,
                'featured': True
            },
            {
                'title': 'Blog Website',
                'description': 'A blog website with a modern design and a responsive layout.',
                'long_description': 'A modern blog website with a modern design and a responsive layout. Built with HTML, CSS, and JavaScript.',
                'technologies': json.dumps(['HTML', 'CSS', 'JavaScript', 'Flask', 'SQLAlchemy', 'Python']),
                'github_url': 'https://github.com/KaustubhMukdam/blog-website',
                'live_demo_url': 'https://kaustubhmukdam.github.io/blog-website',
                'image_url': None,
                'featured': True
            }
        ]
        
        for project_data in projects_data:
            exists = Project.query.filter_by(title=project_data['title']).first()
            if not exists:
                db.session.add(Project(**project_data))
        
        # Sample Experience - Learning Journey & Achievements
        experience_data = [
            {
                'company': 'IBM Machine Learning Specialization',
                'position': 'Machine Learning Student',
                'start_date': date(2025, 9, 3),
                'end_date': None,
                'description': 'Currently pursuing IBM Machine Learning Professional Certificate on Coursera. Learning advanced machine learning concepts, data analysis, and AI applications.',
                'technologies': json.dumps(['Python', 'Machine Learning', 'Data Science', 'AI', 'Statistics']),
                'location': 'Online - Coursera'
            },
            {
                'company': '100 Days of Python Programming',
                'position': 'Python Developer Course Graduate',
                'start_date': date(2024, 7, 10),
                'end_date': date(2025, 9, 3),
                'description': 'Completed comprehensive Python programming course by Dr. Angela Yu on Udemy. Built 100+ projects including web applications, games, and automation tools.',
                'technologies': json.dumps(['Python', 'Flask', 'Django', 'Web Scraping', 'APIs', 'Databases']),
                'location': 'Online - Udemy'
            },
            {
                'company': 'Hackathon Participant',
                'position': 'Competitive Programmer & Developer',
                'start_date': date(2025, 7, 10),
                'end_date': None,
                'description': 'Active participant in various hackathons and coding competitions. Developed innovative solutions and collaborated with teams to solve real-world problems.',
                'technologies': json.dumps(['Python', 'AI', 'HTML/CSS', 'APIs', 'Problem Solving', 'Machine Learning']),
                'location': 'Various Locations'
            }
        ]
        
        for exp_data in experience_data:
            exists = Experience.query.filter_by(company=exp_data['company'], position=exp_data['position']).first()
            if not exists:
                db.session.add(Experience(**exp_data))
        
        # Sample Blog Posts
        blog_posts_data = [
            {
                'title': 'Getting Started with Modern Web Development',
                'slug': 'getting-started-modern-web-development',
                'content': '# Getting Started with Modern Web Development\n\nWeb development has evolved significantly over the years...',
                'excerpt': 'A comprehensive guide for beginners who want to start their journey in modern web development.',
                'published': True,
                'featured': True,
                'tags': json.dumps(['Web Development', 'Beginner', 'Tutorial', 'HTML', 'CSS', 'JavaScript'])
            },
            {
                'title': 'Building Scalable React Applications',
                'slug': 'building-scalable-react-applications',
                'content': '# Building Scalable React Applications\n\nScalability is crucial for modern web applications...',
                'excerpt': 'Learn how to structure and organize your React applications for better scalability and maintainability.',
                'published': True,
                'featured': True,
                'tags': json.dumps(['React', 'JavaScript', 'Architecture', 'Performance'])
            },
            {
                'title': 'The Future of Web Development',
                'slug': 'future-web-development',
                'content': '# The Future of Web Development\n\nThe web development landscape is constantly evolving...',
                'excerpt': 'Exploring emerging trends and technologies that will shape the future of web development.',
                'published': True,
                'featured': False,
                'tags': json.dumps(['Web Development', 'Future', 'Technology', 'Trends'])
            },
            {
                'title': 'Mastering CSS Grid and Flexbox',
                'slug': 'mastering-css-grid-flexbox',
                'content': '# Mastering CSS Grid and Flexbox\n\nCSS Grid and Flexbox are powerful layout tools...',
                'excerpt': 'A deep dive into CSS Grid and Flexbox for creating modern, responsive layouts.',
                'published': True,
                'featured': False,
                'tags': json.dumps(['CSS', 'Layout', 'Grid', 'Flexbox', 'Responsive Design'])
            }
        ]
        
        for post_data in blog_posts_data:
            exists = BlogPost.query.filter_by(slug=post_data['slug']).first()
            if not exists:
                db.session.add(BlogPost(**post_data))
        
        # Sample Testimonials
        # testimonials_data = [
        #     {
        #         'name': 'Sarah Johnson',
        #         'position': 'Product Manager',
        #         'company': 'TechCorp',
        #         'content': 'Kaustubh is an exceptional developer with great attention to detail. His code is clean, well-documented, and he always delivers on time.',
        #         'rating': 5,
        #         'image_url': None,
        #         'approved': True
        #     },
        #     {
        #         'name': 'Michael Chen',
        #         'position': 'CTO',
        #         'company': 'InnovateLab',
        #         'content': 'Working with Kaustubh was a pleasure. He brought innovative solutions to complex problems and helped our team grow significantly.',
        #         'rating': 5,
        #         'image_url': None,
        #         'approved': True
        #     },
        #     {
        #         'name': 'Emily Rodriguez',
        #         'position': 'Design Lead',
        #         'company': 'CreativeStudio',
        #         'content': 'Kaustubh has an excellent understanding of both frontend and backend development. His collaborative approach made our projects successful.',
        #         'rating': 5,
        #         'image_url': None,
        #         'approved': True
        #     }
        # ]
        
        # for testimonial_data in testimonials_data:
        #     testimonial = Testimonial(**testimonial_data)
        #     db.session.add(testimonial)
        
        # Commit all changes
        db.session.commit()
        
        print("✅ Sample data created successfully!")
        print(f"📊 Created {len(skills_data)} skills")
        print(f"🚀 Created {len(projects_data)} projects")
        print(f"💼 Created {len(experience_data)} experience entries")

if __name__ == '__main__':
    create_sample_data()
