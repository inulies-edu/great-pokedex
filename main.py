from flask_cors import CORS
from flask import jsonify
from instance.db import db
from server.instance import server
from modules.api.api import api
from modules.pokedex.pokedex import pokedex
from modules.login.login import login
from modules.admin.admin import admin

app = server.app
CORS(app)

app.register_blueprint(api)
app.register_blueprint(pokedex)
app.register_blueprint(login)
app.register_blueprint(admin)


if __name__ == '__main__':
    db.init_app(app)
    server.run()