#!/usr/bin/env python3
"""
Customize your experience data with your actual hackathons and achievements
"""

from app import create_app, db
from app.models import Experience
from datetime import datetime, date
import json

def customize_experience():
    """
    Customize this function with your actual experiences:
    - Specific hackathons you've participated in
    - Projects you've built during courses
    - Any certifications or achievements
    - Personal projects
    """
    
    app = create_app()
    
    with app.app_context():
        # Clear existing experience data
        Experience.query.delete()
        
        # CUSTOMIZE THESE WITH YOUR ACTUAL EXPERIENCES:
        
        # 1. Current Learning (IBM Machine Learning)
        current_learning = Experience(
            company='IBM Machine Learning Specialization',
            position='Machine Learning Student',
            start_date=date(2024, 1, 1),  # Update with your actual start date
            end_date=None,  # Ongoing
            description='Currently pursuing IBM Machine Learning Professional Certificate on Coursera. Learning advanced machine learning concepts, data analysis, and AI applications.',
            technologies=json.dumps(['Python', 'Machine Learning', 'Data Science', 'AI', 'Statistics', 'Pandas', 'NumPy', 'Scikit-learn']),
            location='Online - Coursera'
        )
        db.session.add(current_learning)
        
        # 2. Python Course Completion
        python_course = Experience(
            company='100 Days of Python Programming',
            position='Python Developer Course Graduate',
            start_date=date(2023, 6, 1),  # Update with your actual dates
            end_date=date(2023, 9, 30),   # Update with your actual completion date
            description='Completed comprehensive Python programming course by Dr. Angela Yu on Udemy. Built 100+ projects including web applications, games, automation tools, and data analysis projects.',
            technologies=json.dumps(['Python', 'Flask', 'Django', 'Web Scraping', 'APIs', 'Databases', 'Beautiful Soup', 'Selenium']),
            location='Online - Udemy'
        )
        db.session.add(python_course)
        
        # 3. ADD YOUR HACKATHON EXPERIENCES HERE:
        # Example format - replace with your actual hackathons:
        
        hackathon_1 = Experience(
            company='[Hackathon Name]',  # e.g., "TechCrunch Disrupt Hackathon"
            position='Participant & Developer',
            start_date=date(2023, 8, 15),  # Update with actual date
            end_date=date(2023, 8, 17),    # Update with actual date
            description='Participated in [Hackathon Name] and developed [Project Description]. [Add details about what you built, technologies used, and any awards or recognition].',
            technologies=json.dumps(['Python', 'React', 'Node.js', 'APIs']),  # Update with actual tech stack
            location='[Location]'  # e.g., "San Francisco, CA" or "Online"
        )
        # db.session.add(hackathon_1)  # Uncomment when you add your hackathon
        
        # 4. ADD MORE HACKATHONS OR ACHIEVEMENTS:
        # Copy the format above for each hackathon or achievement
        
        # 5. Personal Projects (if significant)
        personal_project = Experience(
            company='Personal Projects',
            position='Independent Developer',
            start_date=date(2023, 1, 1),  # Update with when you started
            end_date=None,  # Ongoing
            description='Developed various personal projects including this portfolio website, automation scripts, and web applications to practice and showcase programming skills.',
            technologies=json.dumps(['Python', 'JavaScript', 'HTML/CSS', 'Flask', 'Git']),
            location='Remote'
        )
        db.session.add(personal_project)
        
        # Commit changes
        db.session.commit()
        
        print("✅ Experience data customized successfully!")
        print("📝 Remember to update the dates and details with your actual experiences")
        print("🏆 Add your specific hackathon experiences by uncommenting and customizing the hackathon entries")

def add_specific_hackathon(hackathon_name, start_date, end_date, description, technologies, location):
    """
    Helper function to add a specific hackathon experience
    """
    app = create_app()
    
    with app.app_context():
        hackathon = Experience(
            company=hackathon_name,
            position='Participant & Developer',
            start_date=start_date,
            end_date=end_date,
            description=description,
            technologies=json.dumps(technologies),
            location=location
        )
        db.session.add(hackathon)
        db.session.commit()
        print(f"✅ Added hackathon: {hackathon_name}")

# Example usage:
# add_specific_hackathon(
#     hackathon_name="TechCrunch Disrupt Hackathon",
#     start_date=date(2023, 8, 15),
#     end_date=date(2023, 8, 17),
#     description="Built a real-time collaboration tool for remote teams. Won 2nd place in the productivity category.",
#     technologies=['React', 'Node.js', 'Socket.io', 'MongoDB'],
#     location="San Francisco, CA"
# )

if __name__ == '__main__':
    customize_experience()
