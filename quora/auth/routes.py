import secrets,  os, math
from typing import Dict
from PIL import Image
from flask import render_template, request, flash, session, redirect, url_for, Blueprint, jsonify
from passlib.hash import sha256_crypt
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required, current_user
from quora.models import Questions, User, db


auths = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auths.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['full_name']
        phone = request.form['phone']
        password = request.form['password']
        confpassword = request.form['confpassword']
        email = request.form['email']
        college = request.form['college_name']
        gender = request.form['gender']
        
        user = User.query.filter_by(email=email).first()
        if not user:            
            if password == confpassword:
                password = sha256_crypt.encrypt(str(password))
                user1 = User(name=fullname, phone=phone, email=email, password=password,
                                gender=gender, college=college)
                db.session.add(user1)
                db.session.commit()
            
                response = {'success' : True, 'message' : 'Your Account is Created Successfully'}
                return jsonify(response)
            else:
                response = {'success' : False, 'message' : "Password does't match"}
                return jsonify(response)
        else:
            response = {'success' : False, 'message' : "Email already registered"}
            return jsonify(response)

@auths.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user:
            db_password = user.password
            if sha256_crypt.verify(password, db_password):
                login_user(user)
                response = {'success' : True, 'message' : f'Hi, {current_user.name} Welcome to Query'}
                return jsonify(response)
            else:
                response = {'success' : False, 'message' : "Password doesn't matches"}
                return jsonify(response)
        else:
            response = {'success' : False, 'message' : "User Doesn't exist"}
            return jsonify(response)

@auths.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@auths.route('/dashboard/')
@login_required
def dashboard():
    user = User.query.filter_by(id=current_user.id).first()
    questions = user.questions

    return render_template('dashboard.html',  questions=questions)

@auths.route('/yourQueries')
@login_required
def yourQueries():
    user = User.query.filter_by(id=current_user.id).first()
    questions = user.questions
    result = []
    for ques in questions:
        dic = {'sno' : ques.id, 'title' : ques.title, 'description' : ques.description, 'posted_on' : ques.posted_on}
        result.append(dic)
    questions = result
    return jsonify(questions)

@auths.route('/yourAnswers')
@login_required
def yourAnswers():
    user = User.query.filter_by(id=current_user.id).first()
    answers = user.answers
    result = []
    for ans in answers:
        dic = {'sno' : ans.id, 'title' : ans.question.title, 'description' : ans.question.description, 'answer' : ans.ans ,'posted_on' : ans.posted_on}
        result.append(dic)
    answers = result
    return jsonify(answers)

@auths.route('/editProfile', methods=['GET', 'POST'])
@login_required
def editProfile():
    return render_template('editProfile.html');





    





