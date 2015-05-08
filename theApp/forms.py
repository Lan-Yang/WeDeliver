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
    ''' User Login form '''
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
                user.passwd,
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
                user.passwd,
                self.passwd.data
                ):
                self.passwd.errors.append(u"Username and password don't match")
                return False

        self.user = user
        return True


class ShipperPostForm(Form):
    '''Shipper post form'''
    passwd = PasswordField('Password', [
                                            DataRequired(message=u"Password is required")
                                            ])
    pickupaddr = StringField('pickupaddr')
    pickuptime = StringField('pickuptime')
    cargosize = StringField('cargosize')
    delivertime = StringField('delivertime')
    stopaddress = StringField('stopaddress')
    expectfee = StringField('expectfee')
    
    
    def __init__(self, *args, **kwargs):
        '''initiate self with request parameters'''
        Form.__init__(self, *args, **kwargs)
    
    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        
        if self.pickupaddr is None:
            return False
        if self.pickuptime is None:
            return False
        if self.cargosize is None:
            return False
        if self.delivertime is None:
            return False
        if self.stopaddress is None:
            return False
        if self.expectfee is None:
            return False
        return True


    def recordPost(self):
        '''insert the post into database'''
        order = Order()
        order.pickupaddr = self.pickupaddr.data
        order.pickuptime = self.pickuptime.data
        order.cargosize = self.cargosize.data
        order.oid = 13
        
        order_record = OrderRecord()
        order_record.sid = 13
        order_record.oid = 13
        order_record.delivertime = self.delivertime.data
        order_record.stopaddress = self.stopaddress.data
        order_record.expectfee = self.expectfee.data

        db_session.add(order)
        db_session.add(order_record)
        db_session.commit()



class SSearchForm(Form):
    ''' Shipper Search form '''
    date = DateField('Date', [
        DataRequired(message=u"Pickup Date is required")
        ], format='%m/%d/%Y')
    depart = StringField('Address', [
        DataRequired(message=u"Address is required")
        ])
    weight = IntegerField('Cargo', [
        DataRequired(message=u"Cargo weight is required")
        ])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.orders = []

    def search(self):
        result = Order.query.filter(Order.pickuptime >= self.date.data)
        self.orders = [x for x in result]