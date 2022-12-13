from flask import Blueprint, render_template

pokedex = Blueprint('pokedex', __name__)

@pokedex.route('/')
def load_page():
    return render_template('pokedex.htm')

