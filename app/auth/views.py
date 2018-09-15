from flask import render_template,redirect,url_for,flash,request,abort
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm,UpdateProfile
from .. import db
from flask_login import login_user,logout_user,login_required
import markdown2

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Email or Password')

    title = " login"
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
    title = "New Account"
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

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@auth.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))





@auth.route('/pitch/add', methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
    View function to create a new pitch
    '''
    form = NewPitch()
    if form.validate_on_submit():


        new_pitch = Pitches(title = form.title.data,pitch = form.a_pitch.data,category = form.category.data)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    title = "I Pitch"

    return render_template('new_pitch.html', title = title, pitch_form = form)

@auth.route('/')
def index():

    '''
    Home page for the blogger
    '''


    return render_template('index.html')