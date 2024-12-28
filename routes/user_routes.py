from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, Follow
from schema import UserSchema 

user_bp = Blueprint('user', __name__)

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_schema = UserSchema()
    return jsonify(user_schema.dump(user)), 200

@user_bp.route('/follow/<int:user_id>', methods=['POST'])
@jwt_required()
def follow_user(user_id):
    current_user_id = get_jwt_identity()
    follow = Follow(follower_id=current_user_id, followed_id=user_id)
    db.session.add(follow)
    db.session.commit()
    return jsonify({'message': 'Followed successfully'})