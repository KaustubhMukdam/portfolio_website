from flask import Blueprint, jsonify, request
from app.models import Project, Skill, Experience, BlogPost, Testimonial

main = Blueprint('main', __name__)

# About Me endpoint
@main.route('/api/about')
def get_about():
    # Return static about me data or from database
    return jsonify({
        'name': 'Kaustubh Devidas Mukdam',
        'title': 'Your Professional Title',
        'bio': 'Your biography...',
        'location': 'Your Location',
        'email': 'your.email@example.com',
        'social_links': {
            'github': 'https://github.com/KaustubhMukdam',
            'linkedin': 'www.linkedin.com/in/kaustubh-mukdam-ab0170340',
            'twitter': 'https://x.com/KMukdam9474'
        }
    })

# Skills endpoint
@main.route('/api/skills')
def get_skills():
    skills = Skill.query.all()
    return jsonify([{
        'id': skill.id,
        'name': skill.name,
        'category': skill.category,
        'proficiency_level': skill.proficiency_level,
        'icon_class': skill.icon_class
    } for skill in skills])

# Experience endpoint
@main.route('/api/experience')
def get_experience():
    experiences = Experience.query.order_by(Experience.start_date.desc()).all()
    return jsonify([{
        'id': exp.id,
        'company': exp.company,
        'position': exp.position,
        'start_date': exp.start_date.isoformat(),
        'end_date': exp.end_date.isoformat() if exp.end_date else None,
        'description': exp.description,
        'technologies': exp.technologies,
        'location': exp.location
    } for exp in experiences])

# Resume download endpoint
@main.route('/api/resume')
def download_resume():
    # Serve resume PDF file
    return send_file('"D:\Kaustubh_Mukdam_Resume.pdf"', as_attachment=True)