from .db import db
from datetime import datetime

class User_Permission(db.Model):
  __tablename__ = 'user_permissions'
  
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  
  # Admin panel access
  is_admin = db.Column(db.Boolean, default=False, nullable=False)
  
  # Permissions for moderating other users and the website
  modify_layout = db.Column(db.Boolean, default=False, nullable=False)
  modify_users_signup = db.Column(db.Boolean, default=False, nullable=False)
  modify_users_comment = db.Column(db.Boolean, default=False, nullable=False)
  modify_users_access = db.Column(db.Boolean, default=False, nullable=False)
  modify_site_settings = db.Column(db.Boolean, default=False, nullable=False)
  modify_site_access = db.Column(db.Boolean, default=False, nullable=False)
  
  # Page access
  page_create = db.Column(db.Boolean, default=False, nullable=False)
  page_update = db.Column(db.Boolean, default=False, nullable=False)
  page_delete = db.Column(db.Boolean, default=False, nullable=False)
  
  # Post acess
  post_create = db.Column(db.Boolean, default=False, nullable=False)
  post_update = db.Column(db.Boolean, default=False, nullable=False)
  post_delete = db.Column(db.Boolean, default=False, nullable=False)
  
  # Comment access
  comment_create = db.Column(db.Boolean, default=True, nullable=False)
  comment_update = db.Column(db.Boolean, default=True, nullable=False)
  comment_delete = db.Column(db.Boolean, default=True, nullable=False)
  
  
  created_at = db.Column(db.DateTime, db.ForeignKey('users.created_at'), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
  
  
  
  def check_admin(self):
    return self.is_admin
  
  @property
  def check_permission(self, perm):
    return getattr(self, perm, None)

  
  @check_permission.setter
  def check_permission(self, perm, value):
    if value in [True, False]:
      setattr(self, perm, value)
      
      
  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'is_admin': self.is_admin,
      'modify_layout': self.modify_layout,
      'modify_users_signup': self.modify_users_signup,
      'modify_users_comment': self.modify_users_comment,
      'modify_users_access': self.modify_users_access,
      'modify_site_settings': self.modify_site_settings,
      'modify_site_access': self.modify_site_access,
      'page_create': self.page_create,
      'page_update': self.page_update,
      'page_delete': self.page_delete,
      'post_create': self.post_create,
      'post_update': self.post_update,
      'post_delete': self.post_delete,
      'comment_create': self.comment_create,
      'comment_update': self.comment_update,
      'comment_delete': self.comment_delete,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
    }