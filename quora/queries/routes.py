import secrets,  os
from PIL import Image
from flask import render_template, request, flash, session, redirect, url_for, Blueprint, jsonify
from flask_login import login_required
from werkzeug.utils import secure_filename
from quora.models import User, db

query = Blueprint('queries', __name__);

@query.route('/askQuery')
@login_required
def askQuery():
    pass