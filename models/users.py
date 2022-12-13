from flask_login import UserMixin
from instance.db import db
from server.instance import server
from werkzeug.security import generate_password_hash, check_password_hash





class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
