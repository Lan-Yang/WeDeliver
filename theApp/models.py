# -*- coding: utf-8 -*-
"""
Models for database of the flask application.
"""

from theApp import app, db
from werkzeug.security import generate_password_hash
from datetime import date

# db.session
db_session = db.session

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)  # auto-inc
    email = db.Column(db.String(80), unique=True)
    paswd = db.Column(db.String(64))
    fstname = db.Column(db.String(64))
    lstname = db.Column(db.String(64))
    gender = db.Column(db.String(8))
    wechat = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    school = db.Column(db.String(96))
    photo = db.Column(db.String(96))  # file path of photo
    discrip = db.Column(db.String(256))
    # houses = db.relationship('House', backref='person', lazy='dynamic')

    def __init__(self, email, paswd):
        self.email = email
        self.paswd = generate_password_hash(paswd)
        self.fstname = ''
        self.lstname = ''
        self.gender = 'Male'
        self.wechat = ''
        self.phone = ''
        self.school = ''
        self.photo = ''
        self.discrip = ''

    def __repr__(self):
        return '<User %r>' % self.email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.uid)  # python 2
