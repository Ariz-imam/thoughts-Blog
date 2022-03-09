import secrets,  os, math, json
from typing import Dict
from PIL import Image
from flask import render_template, request, flash, redirect, session, url_for, Blueprint, jsonify
from passlib.hash import sha256_crypt
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required, current_user
from quora.models import Questions, User, db
from quora import app, mail


auths = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

@auths.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['full_name']
        phone = request.form['phone']
        password = request.form['password']
        confpassword = request.form['confpassword']
        email = request.form['email']
        profession = request.form['college_name']
        gender = request.form['gender']
        
        user = User.query.filter_by(email=email).first()
        if not user:            
            if password == confpassword:
                password = sha256_crypt.encrypt(str(password))
                user1 = User(name=fullname, phone=phone, email=email, password=password,
                                gender=gender, profession=profession)
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
    flash('You are successfully logged out.', 'info')
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
        dic = {'id' : ques.id, 'title' : ques.title, 'description' : ques.description, 'posted_on' : ques.posted_on}
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
        dic = {'id' : ans.question.id, 'title' : ans.question.title, 'description' : ans.question.description, 'answer' : ans.ans ,'posted_on' : ans.posted_on}
        result.append(dic)
    answers = result
    return jsonify(answers)

@auths.route('/editProfile', methods=['GET', 'POST'])
@login_required
def editProfile():
    if request.method == 'POST':
        fullname = request.form['full_name']
        phone = request.form['phone']
        profession = request.form['college_name']        
        city = request.form['city']        
        country = request.form['country']        
        gender = request.form['gender']

        user = User.query.filter_by(id=current_user.id).first()
        user.name = fullname
        user.phone = phone
        user.profession = profession
        user.city = city
        user.country = country
        user.gender = gender
        db.session.commit()
        response = {'success' : True, 'message' : 'Your Account is Successfully Updated'}
        return jsonify(response)

    return render_template('editProfile.html')

@auths.route('/delete_account/<int:user_id>')
@login_required
def deleteAccount(user_id):
    try:
        user = User.query.filter_by(id=user_id).first();
        db.session.delete(user)
        db.session.commit()
        response = {'success' : True, 'message' : 'Your Account is Successfully deleted'}
    except:
        response = {'success' : False, 'message' : 'Something went wrong.'}

    return jsonify(response)
     
@auths.route('/viewProfileGetQueries/<int:id>')
def viewProfileGetQueries(id):
    user = User.query.filter_by(id=id).first()
    questions = user.questions
    result = []
    for ques in questions:
        dic = {'id' : ques.id, 'title' : ques.title, 'description' : ques.description, 'posted_on' : ques.posted_on}
        result.append(dic)
    questions = result
    return jsonify(questions)

@auths.route('/viewProfileGetAnswers/<int:id>')
def viewProfileGetAnswers(id):
    user = User.query.filter_by(id=id).first()
    answers = user.answers
    result = []
    for ans in answers:
        dic = {'id' : ans.question.id, 'title' : ans.question.title, 'description' : ans.question.description, 'answer' : ans.ans ,'posted_on' : ans.posted_on}
        result.append(dic)
    answers = result
    return jsonify(answers)

@auths.route('/reset_request', methods=['POST', 'GET'])
def reset_request():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email = email).first()
        if user is None:
            response = {'success' : False, 'message' : 'You haven\'t any account. Please create an account first'}
            return jsonify(response)
        else:
            token = user.get_reset_token()
            mail.send_message(
                "Reset Password Email",
                sender=params['gmail-user'],
                recipients = [user.email],
                body=f'''To reset your password visit the following link:
{url_for('auth.reset_password_token', token=token, _external=True)}

if you didn't make this request then simply ignore this email no changes will be made.
'''
            )
            response = {'success' : True, 'message' : 'A mail has been sent in your email to reset password. Press OK to continue'}
            return jsonify(response)
    

    user = User.query.filter_by(email = current_user.email).first()
    token = user.get_reset_token()
    mail.send_message(
        "Reset Password Email",
        sender=params['gmail-user'],
        recipients = [user.email],
        body=f'''To reset your password visit the following link:
{url_for('auth.reset_password_token', token=token, _external=True)}

if you didn't make this request then simply ignore this email no changes will be made.
'''
            )
    flash('A mail has been sent in your email to reset password.', 'info')
    return redirect(url_for('auth.logout'))
    


@auths.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_password_token(token):
    if request.method == "POST":
        password = request.form['password']
        confpassword = request.form['confpassword']

        if password == confpassword:
            password = sha256_crypt.encrypt(str(password))
            user = User.verify_reset_token(token)
            user.password = password
            db.session.commit()
            response = {'success' : True, 'message' : 'Your password is updated successfully. Please re-login with email new password'}
            return jsonify(response)
        else:
            response = {'success' : False, 'message' : 'Confirm password doesn\'t match to new password. Please enter password attentively.'}
            return jsonify(response) 
        
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('home'))

    return render_template('resetPassword.html', token=token)

@auths.route('/reset_password', methods=['GET', 'POST'])
@login_required
def reset_password():
    if request.method == "POST":
        password = request.form['password']
        newpassword = request.form['newpassword']
        confpassword = request.form['confpassword']

        user = User.query.filter_by(email=current_user.email).first()

        db_password = user.password

        if sha256_crypt.verify(password, db_password):
            if newpassword == confpassword:
                newpassword = sha256_crypt.encrypt(str(newpassword))
                user.password = newpassword
                db.session.commit()
                response = {'success' : True, 'message' : 'Your password is updated successfully.'}
                return jsonify(response)
            else:
                response = {'success' : False, 'message' : 'Confirm password doesn\'t match to new password. Please enter password attentively.'}
                return jsonify(response)  
        else:
            response = {'success' : False, 'message' : 'Your account\'s password entered is wrong'}
            return jsonify(response)  











    





