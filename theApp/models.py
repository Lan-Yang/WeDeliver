# -*- coding: utf-8 -*-
"""
Models for database of the flask application.
"""

from theApp import app, db
from werkzeug.security import generate_password_hash


# db.session
db_session = db.session


class Order(db.Model):
    oid = db.Column(db.Integer, primary_key=True)  # auto-inc
    pickupaddr = db.Column(db.String(128))
    pickuptime = db.Column(db.DateTime)
    did = db.Column(db.Integer)
    cargosize = db.Column(db.Integer)
    trucksize = db.Column(db.Integer)
    totalfee = db.Column(db.Float)
    basefee = db.Column(db.Float)
    closefee = db.Column(db.Float)
    status = db.Column(db.String(4))
    drivername = db.Column(db.String(32))
    driverphone = db.Column(db.String(16))

    def __repr__(self):
        return '<Order %r>' % self.oid


class OrderRecord(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer, primary_key=True)
    did = db.Column(db.Integer)
    stopaddress = db.Column(db.String(128))
    delivertime = db.Column(db.DateTime)
    cargosize = db.Column(db.Integer)
    fee = db.Column(db.Float)
    acceptedtime = db.Column(db.Float)  # DateTime?
    status = db.Column(db.String(4))
    grade = db.Column(db.Float)
    commet = db.Column(db.Text)  # comment

    def __repr__(self):
        return '<OrderRecord %s, %s>' % (self.oid, self.sid)


class Shipper(db.Model):
    sid = db.Column(db.Integer, primary_key=True)  # auto-inc
    name = db.Column(db.String(32))
    passwd = db.Column(db.String(128))
    email = db.Column(db.String(32))
    phone = db.Column(db.String(32))
    addr_1 = db.Column(db.String(64))
    addr_2 = db.Column(db.String(64))
    city = db.Column(db.String(32))
    state = db.Column(db.String(16))
    zip = db.Column(db.String(32))

    def __repr__(self):
        return '<Shipper %r>' % self.sid

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.sid)  # python 2


class Deliverer(db.Model):
    did = db.Column(db.Integer, primary_key=True)  # auto-inc
    name = db.Column(db.String(32))
    passwd = db.Column(db.String(128))
    email = db.Column(db.String(32))
    phone = db.Column(db.String(32))
    addr_1 = db.Column(db.String(64))
    addr_2 = db.Column(db.String(64))
    city = db.Column(db.String(32))
    state = db.Column(db.String(16))
    zip = db.Column(db.String(32))
    grade = db.Column(db.Float)

    def __repr__(self):
        return '<Deliver %r>' % self.did

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.did)  # python 2
