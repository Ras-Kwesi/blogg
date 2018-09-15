from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo
from..models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError,TextAreaField





class SubscribeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    Name =  StringField('Your Username Please',validators=[Required(),Email()])
    submit = SubmitField('Sign In')

class CommentForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    Name =  StringField('Your Username Please',validators=[Required(),Email()])
    submit = SubmitField('Sign In')


