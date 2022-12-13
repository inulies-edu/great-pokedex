from flask import Flask
from flask_login import LoginManager
from models.users import User
import os

class Server():
    def __init__(self) -> None:
        self.app = Flask(__name__, static_folder='../public', template_folder='../public/templates')
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemon.db'
        self.app.config['SECRET_KEY'] = os.urandom(12)
        self.login_manager = LoginManager()
        self.login_manager.init_app(self.app)

    def run(self):
        self.app.run(
            port=5000,
            debug=False
        )

server = Server()