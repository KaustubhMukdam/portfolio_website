from flask import Blueprint, jsonify, request
from app.models import Project, Skill, Experience, BlogPost, Testimonial
from flask import send_file, current_app, send_from_directory
import os

main = Blueprint('main', __name__)

# About Me endpoint
@main.route('/api/about')
def get_about():
    # Return static about me data or from database
    return jsonify({
        'name': 'Kaustubh Devidas Mukdam',
        'title': 'Aspiring Machine Learning Engineer | Future AI Engineer',
        'bio': 'I am a passionate and dedicated Machine Learning Engineer with a strong foundation in machine learning algorithms, data analysis, and AI applications. I am currently pursuing a Bachelor of Technology in Computer Science and Engineering at the Vishwakarma Institute of Technology, Pune. I am interested in building AI applications that can help solve real-world problems and improve people\'s lives.',
        'location': 'Pune, Maharashtra, India',
        'image_url': '/static/profile.jpg',
        'email': 'kaustubhmukdam7@gmail.com',
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
    # Serve resume PDF safely from the app static directory
    static_dir = os.path.join(current_app.root_path, 'static')
    filename = 'Kaustubh_Mukdam_Resume.pdf'
    try:
        return send_from_directory(static_dir, filename, as_attachment=True, download_name=filename)
    except FileNotFoundError:
        return jsonify({'error': 'Resume not found'}), 404