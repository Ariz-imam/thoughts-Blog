import secrets,  os, math
from PIL import Image
from flask import render_template, request, flash, safe_join, session, redirect, url_for, Blueprint, jsonify
from flask_login import login_required, current_user
from quora.models import Answers, Questions, User, db
from quora import mail
from bs4 import BeautifulSoup

query = Blueprint('queries', __name__, template_folder='templates')

def sanitize_html(value):

    soup = BeautifulSoup(value)

    for tag in soup.findAll(True):
        tag.hidden = True

    return str(soup.renderContents())

@query.route('/askQuery', methods=['GET', 'POST'])
@login_required
def askQuery():
    if request.method == 'POST':
        print("askquery")
        try:
            title = request.form['title']
            ques = request.form['description']
            posted_by = current_user.id

            ques = Questions(title=title, description=ques, posted_by=posted_by)
            db.session.add(ques)
            db.session.commit()

            response = {'success' : True, 'message' : 'Your Query is posted successfully'}

            return jsonify(response)

        except:
            response = {'success' : True, 'message' : 'Ooops! Something Went Wrong'}
            return jsonify(response)

NO_OF_QUES = 5
@query.route('/writeAnswer/', methods=['GET', 'POST'])
def writeAnswer():
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

    return render_template('queries.html',  questions=questions, prev=prev, next=next)

@query.route('/answer/ques=<int:id>', methods=['GET', 'POST'])
def answer(id):
    if request.method == 'POST':
        ans = request.form['answer']
        answer = Answers(ans_of=id, ans=ans, posted_by=current_user.id)
        db.session.add(answer)
        db.session.commit()
        question = Questions.query.filter_by(id=id).first()
        mail.send_message('Your Query has been answered by '+current_user.name,
                          sender=current_user.email,
                          recipients = [question.author.email],
                          body = 'Your Question : \n'+str(sanitize_html(question.description)) + "\n\n" + 'Answer : \n'+str(sanitize_html(ans))+
                          "\n\nFrom\n"+current_user.name
                          )
        response = {'success' : True, 'message' : 'Your answer for this question is submited successfully'}
        return jsonify(response)

    question = Questions.query.filter_by(id=id).first()
    answers = list(question.answers)
    return render_template('query.html', question=question, answers=answers)

@query.route('/edit/ques/<int:id>', methods=['GET', 'POST'])
@login_required
def editQuery(id):
    if request.method == 'POST':
        try:
            title = request.form['title']
            desc = request.form['updatedesc']
            question = Questions.query.filter_by(id=id).first()
            question.title = title
            question.description = desc
            db.session.commit()
            response = {'success' : True, 'message' : 'Your query is successfully updated.'}
            return jsonify(response)
        except:
            response = {'success' : False, 'message' : 'Something Went Wrong!!!'}
            return jsonify(response)


    question = Questions.query.filter_by(id=id).first()
    return render_template('editQuery.html', question=question)


@query.route('/delete/ques/<int:id>')
@login_required
def deleteQuery(id):
    question = Questions.query.filter_by(id=id).first()
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('auth.dashboard'))

@query.route('/edit/ans/<int:id>', methods=['GET', 'POST'])
@login_required
def editAnswer(id):
    answer = Answers.query.filter_by(id=id).first()
    if request.method == 'POST':
        ans = request.form['answer']
        answer.ans = ans
        db.session.commit()
        response = {'success' : True, 'message' : 'Your answer for this question is successfully updated.'}
        return jsonify(response)

    question = answer.question
    return render_template('editAnswer.html', question=question, answer=answer)

@query.route('/delete/ans/<int:id>')
@login_required
def deleteAnswer(id):
    answer = Answers.query.filter_by(id=id).first()
    db.session.delete(answer)
    db.session.commit()
    return redirect(url_for('auth.dashboard'))

@query.route('/dashboard/<int:id>')
def viewProfile(id):
    if current_user.is_authenticated and id == current_user.id:
        return redirect(url_for('auth.dashboard'))
    user = User.query.filter_by(id = id).first()
    return render_template('viewProfile.html', user=user)


