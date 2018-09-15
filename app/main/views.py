from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Comments, Blog, Mailer
from .. import db,photos
# from .forms import
from flask_login import login_required,current_user
import markdown2

@main.route('/home')
def home():
    '''
    View function to render the index html template, that directs users to select their log in
    '''

    return render_template('home.html')

@main.route('/post/<int:id>')
def blogpost(id):
    '''
    View function to view a pitch
    '''
    the_blogpost = Blog.query.get(id)
    if the_blogpost is None:
        abort(404)

    the_pitches = markdown2.markdown(the_blogpost.pitch, extras=["code-friendly", "fenced-code-blocks"])
    commentss = Comments.get_comments(id)

    return render_template('post.html')



@main.route('/')
def index():

    '''
    Home page for the blogger
    '''

    blogs = Blog.query.all()


    return render_template('index.html',blogs = blogs)