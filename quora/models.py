from mimetypes import init
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from quora import app
from dotenv import load_dotenv
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from quora import login_manager
from flask_login import UserMixin

load_dotenv()

username = os.environ.get("MY_USERNAME")
password = os.environ.get("MY_PASSWORD") 
db_name = os.environ.get("MY_DB") 
host = os.environ.get("MY_HOST") 

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@{host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


class Answers(db.Model):
    __tablename__ = "answers"
    id = db.Column('id', db.Integer, primary_key=True)
    ans_of = db.Column('ans_of', db.Integer, db.ForeignKey('questions.id'), nullable=False)
    ans = db.Column('ans', db.String(1000), nullable=False)
    posted_by = db.Column('post_by', db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    posted_on = db.Column('post_on', db.DateTime, nullable=True, default=datetime.now())


class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('ques_title', db.String(255), nullable=False)
    description = db.Column('ques_desc', db.String(500), nullable=False)
    posted_on = db.Column('post_on', db.DateTime, nullable=True, default=datetime.now())
    posted_by = db.Column('post_by', db.Integer, db.ForeignKey('users.user_id'), nullable=False,)
    answers = db.relationship('Answers', backref='question', cascade="all, delete-orphan", lazy=True)


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

login_manager.login_view = "home"

login_manager.login_message = "User needs to be logged in to view this page"

login_manager.login_message_category = "warning"


class User(db.Model, UserMixin):

    __tablename__ = "users"
        
    id = db.Column('user_id', db.Integer, primary_key=True, nullable=False)
    name = db.Column('fullname', db.String(255), nullable=False)
    phone = db.Column('phone', db.Integer, nullable=False)
    email = db.Column('email', db.String(255), nullable=False, unique=True)
    password = db.Column('pass', db.String(255), nullable = False)
    gender = db.Column('gender', db.String(255), nullable = False)
    profession = db.Column('profession', db.String(255), nullable = False)
    city = db.Column('city', db.String(255), nullable = True)
    country = db.Column('country', db.String(255), nullable = True)
    pic = db.Column('pic', db.LargeBinary, nullable = True)
    questions = db.relationship('Questions', backref='author', cascade="all, delete-orphan", lazy=True)
    answers = db.relationship('Answers', backref='author', cascade="all, delete-orphan", lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.filter_by(id=user_id).first()






    