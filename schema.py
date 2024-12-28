from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    bio = fields.Str(allow_none=True)
    profile_image = fields.Str(allow_none=True)
    created_at = fields.DateTime(dump_only=True)

class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    caption = fields.Str(allow_none=True)
    image_video_url = fields.Str(required=True)
    background_music = fields.Str(allow_none=True)
    category = fields.Str(validate=validate.Length(max=50), allow_none=True)
    datetime_posted = fields.DateTime(dump_only=True)
    user_id = fields.Int(required=True)

class LikeSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    post_id = fields.Int(required=True)

class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    post_id = fields.Int(required=True)
    content = fields.Str(required=True)
    datetime_posted = fields.DateTime(dump_only=True)