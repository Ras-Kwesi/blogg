from flask_wtf import FlaskForm
from wtforms.validators import Required,Email,EqualTo
from..models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError,TextAreaField





class SubscribeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    name =  StringField('Your Username Please',validators=[Required(),Email()])
    submit = SubmitField('Sign Me Up', validators=[Required()])

class CommentForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    comment = TextAreaField("You're thoughts on this post: ",validators=[Required(),Email()])
    submit = SubmitField('Comment', validators=[Required()])


