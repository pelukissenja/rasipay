from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from models.user import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Konfirmasi Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Daftar")

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValueError("Username sudah digunakan!")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValueError("Email sudah terdaftar!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
