from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from database import db

# Association table for followers
followers_table = Table(
    'followers', db.metadata,
    Column('id', Integer, primary_key=True),
    Column('follower_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('followed_id', Integer, ForeignKey('users.id'), nullable=False)
)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    bio = Column(Text, nullable=True)
    profile_image = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship('Post', back_populates='user', cascade='all, delete-orphan')
    followers = relationship(
        'User',
        secondary=followers_table,
        primaryjoin=id == followers_table.c.followed_id,
        secondaryjoin=id == followers_table.c.follower_id,
        backref='following'
    )

class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(Text, nullable=True)
    image_video_url = Column(String(255), nullable=False)
    background_music = Column(String(255), nullable=True)
    category = Column(String(50), nullable=True)
    datetime_posted = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='posts')
    likes = relationship('Like', back_populates='post', cascade='all, delete-orphan')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')

class Like(db.Model):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    user = relationship('User')
    post = relationship('Post', back_populates='likes')

class Comment(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    content = Column(Text, nullable=False)
    datetime_posted = Column(DateTime, default=datetime.utcnow)

    user = relationship('User')
    post = relationship('Post', back_populates='comments')