from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from ..models import User

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    #username=StringField('Username',validators =[Required(),Length(1,64),Regexp('^[A-Z1-z][A-Za-z0-9]*$',0,'username must have letters,numbers,dots or underscores')]
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    username=StringField('Username',validators =[Required(),Length(1,64),Regexp('^[A-Z1-z][A-Za-z0-9]*$',0,'username must have letters,numbers,dots or underscores')])
    password = PasswordField('Password',validators=[Required(),EqualTo('password2',message='password must match.')])
    password2 = PasswordField('Confirm password',validators=[Required()])
    submit = SubmitField('Log in')
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationErroe('Email already registered')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')
