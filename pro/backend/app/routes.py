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
        db = get_db()
        users = db.execute(
            'SELECT username, score FROM user'
        ).fetchall()

        users = [ {"username": user["username"], "score": user["score"]} for user in users ]

        if users:
            return make_response(jsonify({ "response": "success", "ranks": users }), 200)

    return make_response(jsonify({ "response": "Empty" }), 400)

