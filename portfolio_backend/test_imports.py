# test_imports.py

def test_imports():
    print("Testing imports...")
    
    try:
        from app import create_app
        print("✓ Successfully imported create_app")
        
        app = create_app('development')
        print("✓ Successfully created app instance")
        
        with app.app_context():
            print("✓ Successfully entered app context")
            
            from app.models import db
            print("✓ Successfully imported db")
            
            from app.models import Project, Skill, Experience, BlogPost, Testimonial, ContactMessage
            print("✓ Successfully imported all models")
            
            # Check what tables SQLAlchemy knows about
            print(f"✓ SQLAlchemy metadata tables: {list(db.metadata.tables.keys())}")
            
            # Try to create tables
            db.create_all()
            print("✓ db.create_all() completed")
            
            # Check what tables actually exist in the database
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"✓ Actual database tables: {tables}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_imports()