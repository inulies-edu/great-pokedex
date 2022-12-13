from flask import Blueprint, render_template, redirect, request
from flask_login import login_user, logout_user
from instance.db import db
from models.users import User
from flask_login import login_required

login = Blueprint('login', __name__, url_prefix='/login')

@login.route('/', methods=['GET'])
def load_page():
    return render_template('login.html')

@login.route('/register', methods=['POST'])
@login_required
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
    return redirect('/admin/login')

@login.route('/auth', methods=['POST'])
def authentication():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()

    if user and user.verify_password(password):
        login_user(user)
        return redirect('/admin')
    elif not user or not user.verify_password(password):
        return redirect('/login')
    

@login.route('/logout')
@login_required
def logout():
    logout_user()
    redirect('/login')