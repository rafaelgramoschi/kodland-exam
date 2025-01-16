# import mimetypes
# mimetypes.add_type('application/javascript', '.js')
# mimetypes.add_type('text/css', '.css')
from flask import Flask, render_template
from . import db
from . import auth

app = Flask(__name__)
app.config['DATABASE'] = './sqlite.db'
db.init_app(app)

app.register_blueprint(auth.bp)


@app.route('/')
def index():
    return render_template('index.html')