from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Comments, Blog, Mailer
from .. import db,photos
from .forms import CommentForm, SubscribeForm
from flask_login import login_required,logout_user,current_user
import markdown2

@main.route('/home')
def home():
    '''
    View function to render the index html template, that directs users to select their log in
    '''

    message = 'Thank You for subscribing. Stay tuned for massive content. Watch this space!'

    return render_template('home.html', message = message)

@main.route('/post/<int:id>')
def blogpost(id):
    '''
    View function to view a pitch
    '''

    user = current_user
    blogpost = Blog.query.get(id)
    if blogpost is None:
        abort(404)



    comments = Comments.get_comments(id)

    return render_template('post.html', blogpost = blogpost, comments = comments, user = user)

@main.route('/pitch/new_comment/<id>', methods = ['GET','POST'])
def new_comments(id):
    '''
    View function to create a new comment to a pitch
    '''
    post = Blog.query.filter_by(id=id).first()
    comment_form = CommentForm()


    if comment_form.validate_on_submit():
        email = Mailer.query.filter_by(emails = comment_form.email.data).first()
        if email is not None:
            new_comment = Comments(comment=comment_form.comment.data, blog_comment=id)
            db.session.add(new_comment)
            db.session.commit()

            return redirect(url_for('main.index'))
    title = 'What do you think about this Post? '

    return render_template('new_comment.html',title = title,form=comment_form, post = post)



@main.route('/')
def index():

    '''
    Home page for the blogger
    '''
    user = current_user
    blogs = Blog.query.all()
    subscription_form = SubscribeForm()
    if subscription_form.validate_on_submit():
        new_subscriber = Mailer(name= subscription_form.name.data, emails = subscription_form.email.data)
        new_subscriber.save_mail()

        return redirect(url_for('main.home'))






    return render_template('index.html',blogs = blogs, subscription = subscription_form, user = user)

