# import mimetypes
# mimetypes.add_type('application/javascript', '.js')
# mimetypes.add_type('text/css', '.css')
from flask import Flask, render_template
import db, auth #prod
#from . import db, auth #dev

app = Flask(__name__)
app.secret_key = 'dev'
app.config['DATABASE'] = './sqlite.db'
db.init_app(app)

app.register_blueprint(auth.bp)


@app.route('/')
def index():
    return render_template('index.html')

