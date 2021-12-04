import secrets,  os
from PIL import Image
from flask import render_template, request, flash, session, redirect, url_for, Blueprint, jsonify
from flask_login import login_required, current_user
from quora.models import Questions, db

query = Blueprint('queries', __name__);

@query.route('/askQuery', methods=['GET', 'POST'])
@login_required
def askQuery():
    if request.method == 'POST':
        title = request.form['title']
        ques = request.form['desc']
        posted_by = current_user.name

        ques = Questions(title=title, description=ques, posted_by=posted_by)
        db.session.add(ques)
        db.session.commit()

        response = {'success' : True, 'message' : 'Your Query is posted successfully'}

        return jsonify(response)


