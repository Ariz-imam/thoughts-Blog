from flask import Flask
import secrets
from flask_mail import Mail
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

login_manager = LoginManager()

app = Flask(__name__)
mail = Mail(app)
marsh = Marshmallow(app)
login_manager.init_app(app)


secret = secrets.token_urlsafe(16)
app.secret_key = secret

from quora import routes
from quora.auth.routes import auths
from quora.queries.routes import query

app.register_blueprint(query)
app.register_blueprint(auths)