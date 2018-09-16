from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo
from..models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError,TextAreaField





class SubscribeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required()])
    name =  StringField('Your Username Please',validators=[Required()])
    submit = SubmitField('Sign Me Up')

class CommentForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required()])
    comment = TextAreaField("You're thoughts on this post: ",validators=[Required()])
    submit = SubmitField('Comment')


