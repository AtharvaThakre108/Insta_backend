from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Post
from database import db
from schema import PostSchema
from utils import paginate

post_bp = Blueprint('post', __name__)

@post_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    try:
        # Parse JSON data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request data is missing or invalid'}), 400
        
        # Validate required fields
        required_fields = ['image_video_url']
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400

        # Get user ID from JWT token
        user_id = get_jwt_identity()

        # Create new Post instance
        post = Post(
            caption=data.get('caption'),
            image_video_url=data['image_video_url'],
            background_music=data.get('background_music'),
            category=data.get('category'),
            user_id=user_id
        )
        
        # Add and commit to the database
        db.session.add(post)
        db.session.commit()

        # Serialize and return the created post
        post_schema = PostSchema()
        return jsonify({'message': 'Post created successfully', 'post': post_schema.dump(post)}), 201

    except Exception as e:
        # Handle unexpected errors
        db.session.rollback()
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    
def get_posts():
    try:
        # Get the page and per_page parameters from the query string
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        # Fetch all posts, paginated
        posts_query = Post.query.order_by(Post.datetime_posted.desc())
        paginated_posts = paginate(posts_query, page, per_page)

        # Serialize the results
        post_schema = PostSchema(many=True)
        return jsonify({
            'posts': post_schema.dump(paginated_posts),
            'page': page,
            'per_page': per_page
        }), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
