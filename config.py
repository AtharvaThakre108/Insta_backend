class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instagram.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your-secret-key'