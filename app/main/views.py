from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Comments, Blog, Mailer
from .. import db,photos
from .forms import CommentForm, SubscribeForm
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

@main.route('/pitch/new_comment/<id>', methods = ['GET','POST'])
def new_comments(id):
    '''
    View function to create a new comment to a pitch
    '''
    pitch = Blog.query.filter_by(id=id).first()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comments(comment=comment_form.comment.data, pitch_comment=id,)
        new_comment.save_comment()

        return redirect(url_for('main.index'))
    title = 'What do you think about that pitch? '

    return render_template('new_comment.html',title = title,form=comment_form, pitch = pitch)



@main.route('/')
def index():

    '''
    Home page for the blogger
    '''
    subscription_form = SubscribeForm()
    if subscription_form.validate_on_submit():
        new_subscriber = Mailer(name= subscription_form.comment.data, emaails = subscription_form.email.data)
        new_subscriber.save_mail()

        return redirect(url_for('main.index'))


    blogs = Blog.query.all()



    return render_template('index.html',blogs = blogs, subscription = subscription_form)