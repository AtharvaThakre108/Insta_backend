from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    created_at = fields.DateTime()

class PostSchema(Schema):
    id = fields.Int()
    caption = fields.Str(required=True)
    image_video_url = fields.Str(required=True)
    background_music = fields.Str()
    category = fields.Str(required=True)
    datetime_posted = fields.DateTime()
    user_id = fields.Int()

class LikeSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    post_id = fields.Int()

class CommentSchema(Schema):
    id = fields.Int()
    content = fields.Str(required=True)
    user_id = fields.Int()
    post_id = fields.Int()
    datetime_commented = fields.DateTime()

class FollowSchema(Schema):
    id = fields.Int()
    follower_id = fields.Int()
    followed_id = fields.Int()
