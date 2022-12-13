from flask import Blueprint, jsonify, Response, request, redirect, abort
from models.pokemon import Pokemon
from instance.db import db


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/all', methods=['GET'])
def get_all():
    data = Pokemon.query.all()
    data_json = []
    for pokemon in data:
        data_json.append(pokemon.to_json())
    return jsonify(data_json)

@api.route('/<int:id>', methods=['GET'])
def get_pokemon(id):
    data = Pokemon.query.filter_by(id=id).first()
    if data is None:
        return Response(), 404
    data_json = data.to_json()
    return jsonify(data_json)

@api.route('/create', methods=['POST'])
def create_pokemon():
    body = request.get_json()
    new_pokemon = Pokemon(name=body['name'], image=body['image'], primary_type=body['primary-type'], secondary_type=body['secondary-type'])
    db.session.add(new_pokemon)
    db.session.commit()
    return redirect('/api/all')

@api.errorhandler(404)
def not_found():
    return jsonify({"error": "Not found"}), 404