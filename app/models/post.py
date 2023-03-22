from .db import db
from datetime import datetime

class Post(db.Model):
  __tablename__ = 'posts'
  
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  user_name = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)
  title = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text)
  location = db.Column(db.Integer, db.ForeignKey('pages.id', nullable=False))
  created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
  
  comments = db.relationship('Comment', backref='comments', cascade='all delete')
  
  
  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'user_name': self.user_name,
      'title': self.title,
      'content': self.content,
      'location': self.location,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }