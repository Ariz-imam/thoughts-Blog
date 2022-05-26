from flask import render_template, request, session, redirect, jsonify
from werkzeug.utils import secure_filename
import json 
import math
from datetime import datetime
from quora.models import Questions, Answers, Contacts, db
from quora import app, mail
from quora.queries.routes import NO_OF_QUES

with open('config.json', 'r') as c:
    params = json.load(c)["params"]


@app.route("/")
def home():
    questions = Questions.query.filter_by().all()
    last = math.ceil(len(questions)/NO_OF_QUES)
    page = request.args.get('Qpage', 1, type=int)
    questions = questions[(page-1)*NO_OF_QUES : (page-1)*NO_OF_QUES+ NO_OF_QUES]
    #Pagination Logic
    #First
    if (last==1):
        prev = "#"
        next = "#"
    elif (page==1):
        prev = "#"
        next = "/writeAnswer/?Qpage="+ str(page+1)
    elif(page==last):
        prev = "/writeAnswer/?Qpage=" + str(page - 1)
        next = "#"
    else:
        prev = "/writeAnswer/?Qpage=" + str(page - 1)
        next = "/writeAnswer/?Qpage=" + str(page + 1)

    return render_template('index.html',  questions=questions, prev=prev, next=next)


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from Query Contacts',
                          sender=email,
                          recipients = [params['gmail-user']],
                          body = message + "\n" + "My phone - "+phone+"\nMy Email - "+email+
                          "\n\nFrom\n"+name
                          )
        response = {'success' : True, 'message' : 'Message sent sucessfully.'}
        return jsonify(response)
        
    return render_template('index.html')