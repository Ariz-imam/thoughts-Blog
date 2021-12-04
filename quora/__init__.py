from flask import Flask
import secrets
from flask_mail import Mail
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
mail = Mail(app)
login_manager.init_app(app)


secret = secrets.token_urlsafe(16)
app.secret_key = secret

from quora import routes
from quora.auth.routes import auths
from quora.queries.routes import query

app.register_blueprint(query)
app.register_blueprint(auths)