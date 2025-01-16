import functools

from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, session, url_for,
    make_response
)
from werkzeug.security import check_password_hash, generate_password_hash
#from flask_cors import cross_origin

from db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=['POST'])
#@cross_origin(origins="*", supports_credentials=True)
def signup():
    if request.method == 'POST':
        data = request.get_json(force=True)
        username = data.get('username')
        password = data.get('password')
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password, score) VALUES (?, ?, 0)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already signed up."
            else:
                return make_response(jsonify({ "response": "success" }), 200)

        flash(error)

    return make_response(jsonify({ "response": f"{error}" }), 400)
    

@bp.route('/users', methods=['GET'])
def users():
    if request.method == 'GET':
        db = get_db()
        error = None
        results = db.execute(
            'SELECT * FROM user'
        ).fetchall()
        users = [tuple(row) for row in results]
        return make_response(jsonify({ "response": users }), 200)

@bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json(force=True)
        username = data.get('username')
        password = data.get('password')
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return make_response(jsonify({ "response": "success", "user": {
                "id": user['id'],
                "score": user['score']
            } }), 200)

        flash(error)

    return make_response(jsonify({ "response": f"{error}" }), 400)


@bp.route('/logout')
def logout():
    session.clear()
    return make_response(jsonify({ "response": "success" }), 200)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return make_response(jsonify({ "response": "Login required." }), 401)
        return view(**kwargs)
    return wrapped_view