from flask import Blueprint, jsonify
from app.models import Post, User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@bp.route('/about')
def about():
    return jsonify({"message": "About page"})


@bp.route('/api/test')
def test():
    return jsonify({"message": "Hello from the backend!"})