from flask_login import UserMixin
from flask import request

from app.models.bases.auth import BaseUsers
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    
    return Users.query.get(int(user_id))

class Users(BaseUsers, UserMixin):
    __bind_key__ = 'sqlite'
