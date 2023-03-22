from .db import db
from datetime import datetime


class Page(db.Model):
  __tablename__ = 'pages'
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(40), nullable=False)
  content = db.Column(db.Text)
  active = db.Column(db.Boolean, nullable=False, default=False)
  created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
  
  @property
  def title(self):
    return self.title
  
  @title.setter
  def title(self, str):
    self.title = str
    
  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'content': self.content,
      'active': self.active,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }
    
    