from flask import Flask
import secrets, os
from dotenv import load_dotenv
from flask_mail import Mail
from flask_login import LoginManager

load_dotenv()

gmail_user = os.environ.get("GMAIL_USER")
gmail_password = os.environ.get("GMAIL_PASSWORD")

login_manager = LoginManager()

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = gmail_user,
    MAIL_PASSWORD = gmail_password
)
mail = Mail(app)
login_manager.init_app(app)


secret = secrets.token_urlsafe(16)
app.secret_key = secret

from quora import routes
from quora.auth.routes import auths
from quora.queries.routes import query

app.register_blueprint(query)
app.register_blueprint(auths)