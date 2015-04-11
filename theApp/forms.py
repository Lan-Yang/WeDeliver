# -*- coding: utf-8 -*-
"""
WTF Form class corresponding to the HTML forms.
"""
from flask.ext.wtf import Form
from flask.ext.login import current_user
from wtforms import StringField, BooleanField, PasswordField, IntegerField, DateField, FloatField
from wtforms.validators import DataRequired, Email, Length, Optional
from werkzeug.security import generate_password_hash, check_password_hash
from .models import *


class LoginForm(Form):
    ''' Shipper Login form '''
    email = StringField('Email', [
        Email(message=u"Invalid email address")
        ])
    passwd = PasswordField('Password', [
        DataRequired(message=u"Password is required")
        ])
    who = StringField('Who', default="shipper")  # True - shipper, False - deliverer

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None
        self.rememberme = False

    def validate(self):
        ''' validate the form '''
        rv = Form.validate(self)
        if not rv:
            return False

        if self.who.data == "shipper":
            user = Shipper.query.filter_by(
                email=self.email.data
                ).first()
            if user is None:
                self.email.errors.append(u"This email not registered")
                return False
            if not check_password_hash(
                user.paswd,
                self.passwd.data
                ):
                self.passwd.errors.append(u"Username and password don't match")
                return False
        else:
            user = Deliverer.query.filter_by(
                email=self.email.data
                ).first()
            if user is None:
                self.email.errors.append(u"This email not registered")
                return False
            if not check_password_hash(
                user.paswd,
                self.passwd.data
                ):
                self.passwd.errors.append(u"Username and password don't match")
                return False

        self.user = user
        return True
