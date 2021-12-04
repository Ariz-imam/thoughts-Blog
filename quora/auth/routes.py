import secrets,  os, math
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

NO_OF_QUES = 3

@auths.route('/dashboard/')
@login_required
def dashboard():
    questions = Questions.query.filter_by().all()
    last = math.ceil(len(questions)/NO_OF_QUES)
    Qpage = request.args.get('Qpage', 1, type=int)
    questions = questions[(Qpage-1)*NO_OF_QUES : (Qpage-1)*NO_OF_QUES+ NO_OF_QUES]
    #Pagination Logic
    #First
    if (last==1):
        prev = "#"
        next = "#"
    elif (Qpage==1):
        prev = "#"
        next = "/dashboard/?Qpage="+ str(Qpage+1)
    elif(Qpage==last):
        prev = "/dashboard/?Qpage=" + str(Qpage - 1)
        next = "#"
    else:
        prev = "/dashboard/?Qpage=" + str(Qpage - 1)
        next = "/dashboard/?Qpage=" + str(Qpage + 1)

    return render_template('dashboard.html',  questions=questions, prev=prev, next=next)




    





