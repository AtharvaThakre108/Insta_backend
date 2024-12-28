from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from database import db, migrate
from routes.auth_routes import auth_bp
from routes.post_routes import post_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)
db.init_app(app)
migrate.init_app(app, db)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(post_bp, url_prefix='/api/posts')
app.register_blueprint(user_bp, url_prefix='/api/users')

if __name__ == '__main__':
    app.run(debug=True)