# app/__init__.py

from flask import Flask
from config import config
from app.extensions import db, migrate, mail, cors

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    cors.init_app(app)
    
    # Import models AFTER db is initialized
    from app import models
    
    # Register blueprints
    from app.routes.main import main
    from app.routes.projects import projects
    from app.routes.blog import blog
    from app.routes.contact import contact
    
    app.register_blueprint(main)
    app.register_blueprint(projects)
    app.register_blueprint(blog)
    app.register_blueprint(contact)
    
    return app