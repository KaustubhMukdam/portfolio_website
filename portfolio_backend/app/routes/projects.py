from flask import Blueprint, jsonify, request
from app.models import Project, db

projects = Blueprint('projects', __name__)

@projects.route('/api/projects')
def get_projects():
    featured_only = request.args.get('featured', 'false').lower() == 'true'
    
    query = Project.query
    if featured_only:
        query = query.filter(Project.featured == True)
    
    projects = query.order_by(Project.created_at.desc()).all()
    
    return jsonify([{
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'long_description': project.long_description,
        'technologies': project.technologies,
        'github_url': project.github_url,
        'live_demo_url': project.live_demo_url,
        'image_url': project.image_url,
        'featured': project.featured,
        'created_at': project.created_at.isoformat()
    } for project in projects])

@projects.route('/api/projects/<int:project_id>')
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify({
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'long_description': project.long_description,
        'technologies': project.technologies,
        'github_url': project.github_url,
        'live_demo_url': project.live_demo_url,
        'image_url': project.image_url,
        'featured': project.featured,
        'created_at': project.created_at.isoformat()
    })