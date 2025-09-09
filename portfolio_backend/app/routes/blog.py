from flask import Blueprint, jsonify, request
from app.models import BlogPost, db

blog = Blueprint('blog', __name__)

@blog.route('/api/blog/posts')
def get_blog_posts():
    published_only = request.args.get('published', 'true').lower() == 'true'
    
    query = BlogPost.query
    if published_only:
        query = query.filter(BlogPost.published == True)
    
    posts = query.order_by(BlogPost.created_at.desc()).all()
    
    return jsonify([{
        'id': post.id,
        'title': post.title,
        'slug': post.slug,
        'excerpt': post.excerpt,
        'tags': post.tags,
        'featured': post.featured,
        'created_at': post.created_at.isoformat(),
        'updated_at': post.updated_at.isoformat()
    } for post in posts])

@blog.route('/api/blog/posts/<slug>')
def get_blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug, published=True).first_or_404()
    return jsonify({
        'id': post.id,
        'title': post.title,
        'slug': post.slug,
        'content': post.content,
        'tags': post.tags,
        'created_at': post.created_at.isoformat(),
        'updated_at': post.updated_at.isoformat()
    })