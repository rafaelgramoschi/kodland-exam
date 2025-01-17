# import mimetypes
# mimetypes.add_type('application/javascript', '.js')
# mimetypes.add_type('text/css', '.css')
from flask import Flask, render_template
import db, auth #prod
#from . import db, auth #dev
from flask import (
    jsonify, render_template, request, session,
    make_response
)

app = Flask(__name__)
app.secret_key = 'dev'
app.config['DATABASE'] = './sqlite.db'
db.init_app(app)

app.register_blueprint(auth.bp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ranks', methods=['GET'])
def ranks():
    if request.method == 'GET':
        dbc = db.get_db()
        users = dbc.execute(
            'SELECT username, score FROM user'
        ).fetchall()

        users = [ {"username": user["username"], "score": user["score"]} for user in users ]

        if users:
            return make_response(jsonify({ "response": "success", "ranks": users }), 200)

    return make_response(jsonify({ "response": "Empty" }), 400)


@app.route('/score', methods=['POST'])
def score():
    if request.method == 'POST':
        data = request.get_json(force=True)
        user_id = data.get('id')
        score = data.get('score')
        dbc = db.get_db()
        error = None

        if not user_id:
            error = 'user_id is required.'
        elif not score:
            error = 'score is required.'

        if error is None:
            try:
                dbc.execute(
                    "UPDATE user SET score = ? WHERE id = ?",
                    (score, user_id),
                )
                dbc.commit()
            except:
                error = f"Database error"
            else:
                return make_response(jsonify({ "response": "success" }), 200)

    return make_response(jsonify({ "response": f"{error}" }), 400)
