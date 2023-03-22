from .db import db
from datetime import datetime

class Comment(db.Model):
  __tablename__ = 'comments'
  
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  user_name = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
  content = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
  
  
  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'user_name': self.user_name,
      'post_id': self.post_id,
      'content': self.content,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }