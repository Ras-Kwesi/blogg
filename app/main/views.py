from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Comments,Post,Role
from .. import db,photos
# from .forms import
from flask_login import login_required,current_user
import markdown2

@main.route('/home')
def home():
    '''
    View function to render the index html template, that directs users to select their log in
    '''

    return render_template('home.html',)

@main.route('/pitch/<int:id>')
def pitch(id):
    '''
    View function to view a pitch
    '''
    the_pitch = Pitches.query.get(id)
    if the_pitch is None:
        abort(404)

    the_pitches = markdown2.markdown(the_pitch.pitch, extras=["code-friendly", "fenced-code-blocks"])
    commentss = Comments.get_comments(id)

    return render_template('pitch.html',pitch = pitch, the_pitch = the_pitch, comments = commentss)