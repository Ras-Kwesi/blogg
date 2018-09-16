from flask import render_template,redirect,url_for,flash,request,abort
from . import auth
from ..models import User, Blog, Comments, Mailer
from .forms import LoginForm,RegistrationForm,UpdateProfile,NewPost
from .. import db,photos
from flask_login import login_user,logout_user,login_required
import markdown2
from flask_login import login_required,current_user
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Email or Password')

    title = " Check in Here"
    return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        user.save_user()
        return redirect(url_for('auth.login'))
    title = "New Account for Bloggers"
    return render_template('auth/register.html',registration_form = form, title = title)

@auth.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.nationaltiy = form.age.data
        user.career = form.career.data
        user.age = form.age.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update_profile.html',form =form)

@auth.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('auth.update_profile',uname=uname))





@auth.route('/post/add', methods = ['GET','POST'])
@login_required
def new_post():
    '''
    View function to create a new pitch
    '''

    user = current_user
    form = NewPost()
    if form.validate_on_submit():


        new_post = Blog(title = form.title.data, post = form.post.data)

        new_post.save_blog()

        mail_message("Welcome to one-pitch", "email/new_post", user.email, user=user)
        return redirect(url_for('main.index'))



    title = "New Post"

    return render_template('new_post.html', title = title, form = form)


@auth.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@auth.route('/delete/<id>')
@login_required
def deleteblog(id):

    '''
    View function to delete our blog post
    '''

    # post = Blog.query.get(id)
    post = Blog.query.filter_by(id=id).first()

    post.delete_blog()

    return redirect(url_for('main.index'))

@auth.route('/delete/comment/<id>')
@login_required
def deletecomment(id):

    '''
    View function to delete our blog post
    '''

    # post = Blog.query.get(id)
    comment = Comments.query.filter_by(id=id).first()

    comment.delete_comment()

    return redirect(url_for('main.index'))


