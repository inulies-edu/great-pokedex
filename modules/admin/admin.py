from flask import Blueprint, render_template, redirect, request
from instance.db import db

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/', methods=['GET'])
def load_page():
    return render_template('admin.html')