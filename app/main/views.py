from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Comments,Post,Role
from .. import db,photos
# from .forms import
from flask_login import login_required,current_user
import markdown2

@main.route('/')
def index():
    '''
    View function to render the index html template, that directs users to select their log in
    '''

    return render_template('index.html',)

