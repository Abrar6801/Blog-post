from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

#POSTFORM
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title",validators=[DataRequired()])
    subtitle = StringField("Subtitle",validators=[DataRequired()])
    author = StringField("Your Name",validators=[DataRequired()])
    img_url = StringField("Blog Image URL",validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

#Register form
class RegisterForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Sign me up!")

#LoginForm
class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Login")

#CommentForm
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Blog comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

    