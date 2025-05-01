from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Remember me!')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")


class WishForm(FlaskForm):
    name = StringField("Wish name", validators=[DataRequired()])
    amount = FloatField("Amount", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired()])
    image = FileField("Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images allowed')])
    submit = SubmitField("Submit")


