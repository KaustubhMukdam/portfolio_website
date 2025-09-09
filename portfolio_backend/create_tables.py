# create_tables.py

from app import create_app
from app.models import db, Project, Skill, Experience, BlogPost, Testimonial, ContactMessage, User

def create_tables():
    app = create_app('development')
    
    with app.app_context():
        print("Creating tables...")
        
        # Create all tables
        db.create_all()
        print("All tables created successfully!")
        
        # Verify tables exist
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tables created: {tables}")

if __name__ == '__main__':
    create_tables()