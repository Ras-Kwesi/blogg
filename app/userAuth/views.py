from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import UserLoginForm,UserRegistrationForm
from .. import db
from flask_login import login_user,logout_user,login_required,current_user
import markdown2


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = UserLoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Email or Password')

    title = " login"
    return render_template('adminAuth/login.html',login_form = login_form,title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        user.save_user()
        return redirect(url_for('adminAuth.login'))
    title = "New Account"
    return render_template('adminAuth/register.html',registration_form = form, title = title)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



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



