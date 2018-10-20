from flask.ext.wtf import form
from wtforms import TextField, PasswordField
from wtforms.validators import required, Length


class LoginForm(form):
    username = TextField('username', validators=[required()])
    password = PasswordField('username', validators=[required()])
