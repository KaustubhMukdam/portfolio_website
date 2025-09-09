# seed_data.py

from app import create_app, db
from app.models import Project, Skill, Experience, BlogPost, Testimonial, ContactMessage, User
from datetime import datetime, date
import json

def seed_database():
    app = create_app('development')
    
    with app.app_context():
        # Import all models to ensure they're registered
        from app import models
        
        # Create all tables (this should work now)
        db.create_all()
        print("Tables created successfully!")
        
        # Sample Skills
        skills_data = [
            {'name': 'Python', 'category': 'Programming Language', 'proficiency_level': 5, 'icon_class': 'fab fa-python'},
            {'name': 'JavaScript', 'category': 'Programming Language', 'proficiency_level': 4, 'icon_class': 'fab fa-js'},
            {'name': 'React', 'category': 'Framework', 'proficiency_level': 4, 'icon_class': 'fab fa-react'},
            {'name': 'Flask', 'category': 'Framework', 'proficiency_level': 5, 'icon_class': 'fas fa-flask'},
            {'name': 'PostgreSQL', 'category': 'Database', 'proficiency_level': 4, 'icon_class': 'fas fa-database'},
            {'name': 'Git & GitHub', 'category': 'Tool', 'proficiency_level': 4, 'icon_class': 'fab fa-git-alt'},
            {'name': 'MySQL', 'category': 'Tool', 'proficiency_level': 3, 'icon_class': 'fab fa-mysql'},
        ]
        
        for skill_data in skills_data:
            skill = Skill(**skill_data)
            db.session.add(skill)
        
        # Sample Projects
        projects_data = [
            {
                'title': 'Portfolio Website',
                'description': 'A responsive portfolio website built with Flask and React',
                'long_description': 'This project showcases my web development skills using modern technologies. The backend is built with Flask and SQLAlchemy, while the frontend uses React with responsive design principles.',
                'technologies': json.dumps(['Python', 'Flask', 'React', 'SQLAlchemy', 'PostgreSQL']),
                'github_url': 'https://github.com/KaustubhMukdam/portfolio_website',
                'live_demo_url': 'https://yourportfolio.com',
                'featured': True
            },
            {
                'title': 'Morse Code Converter (GUI and Sound)',
                'description': 'A Text to Morse Code Converter with Morse Code sound and interactive GUI',
                'long_description': 'Built a comprehensive Text to Morse code converter with the help of Python, Tkinter for GUI and WinSound for sound',
                'technologies': json.dumps(['Python', 'Tkinter', 'WinSound']),
                'github_url': 'https://github.com/KaustubhMukdam/morse-code-converter-gui',
                'featured': True
            },
            {
                'title': 'Data Visualization Dashboard',
                'description': 'Interactive dashboard for visualizing sales data',
                'long_description': 'Created an interactive dashboard using D3.js and Chart.js to visualize complex sales data. Features include filtering, real-time updates, and export functionality.',
                'technologies': json.dumps(['Python', 'Flask', 'D3.js', 'Chart.js', 'Pandas']),
                'github_url': 'https://github.com/yourusername/data-dashboard',
                'featured': False
            }
        ]
        
        for project_data in projects_data:
            project = Project(**project_data)
            db.session.add(project)
        
        # Sample Experience
        experiences_data = [
            {
                'company': 'Tech Solutions Inc.',
                'position': 'Full Stack Developer',
                'start_date': date(2022, 1, 15),
                'end_date': None,  # Current position
                'description': 'Developing and maintaining web applications using Python, Flask, and React. Collaborated with cross-functional teams to deliver high-quality software solutions.',
                'technologies': json.dumps(['Python', 'Flask', 'React', 'PostgreSQL', 'Docker']),
                'location': 'Remote'
            },
            {
                'company': 'StartupXYZ',
                'position': 'Junior Developer',
                'start_date': date(2020, 6, 1),
                'end_date': date(2021, 12, 31),
                'description': 'Built responsive web applications and RESTful APIs. Participated in code reviews and agile development processes.',
                'technologies': json.dumps(['JavaScript', 'Node.js', 'MongoDB', 'Express.js']),
                'location': 'New York, NY'
            }
        ]
        
        for exp_data in experiences_data:
            experience = Experience(**exp_data)
            db.session.add(experience)
        
        # Sample Blog Posts
        blog_posts_data = [
            {
                'title': 'Building a REST API with Flask',
                'slug': 'building-rest-api-flask',
                'content': 'In this post, I\'ll walk through the process of building a robust REST API using Flask and SQLAlchemy. We\'ll cover routing, database models, serialization, and best practices for API design...',
                'excerpt': 'Learn how to build a REST API with Flask from scratch, covering all the essential concepts and best practices.',
                'published': True,
                'featured': True,
                'tags': json.dumps(['Flask', 'Python', 'API', 'Backend'])
            },
            {
                'title': 'React State Management Patterns',
                'slug': 'react-state-management-patterns',
                'content': 'State management in React can be challenging as your application grows. In this article, we\'ll explore different patterns and tools for managing state effectively...',
                'excerpt': 'Explore different patterns for managing state in React applications as they scale.',
                'published': True,
                'featured': False,
                'tags': json.dumps(['React', 'JavaScript', 'State Management', 'Frontend'])
            }
        ]
        
        for post_data in blog_posts_data:
            blog_post = BlogPost(**post_data)
            db.session.add(blog_post)
        
        # Sample Testimonials
        testimonials_data = [
            {
                'name': 'John Smith',
                'position': 'Project Manager',
                'company': 'Tech Corp',
                'content': 'Excellent work on our web application. Great attention to detail and delivered on time.',
                'rating': 5,
                'approved': True
            },
            {
                'name': 'Sarah Johnson',
                'position': 'CTO',
                'company': 'Innovation Labs',
                'content': 'Outstanding technical skills and great communication. Would definitely work together again.',
                'rating': 5,
                'approved': True
            }
        ]
        
        for testimonial_data in testimonials_data:
            testimonial = Testimonial(**testimonial_data)
            db.session.add(testimonial)
        
        # Commit all changes
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()