# -*- coding: utf-8 -*-
"""
Models for database of the flask application.
"""

from theApp import app, db
from werkzeug.security import generate_password_hash
from .util import *
from flask.ext.login import UserMixin

# db.session
db_session = db.session


class Order(db.Model):
    oid = db.Column(db.Integer, primary_key=True)  # auto-inc
    title = db.Column(db.String(128))
    pickupaddr = db.Column(db.String(128))
    pickuptime = db.Column(db.DateTime)
    did = db.Column(db.Integer)
    totalcargosize = db.Column(db.Integer)
    trucksize = db.Column(db.Integer)
    initialfee = db.Column(db.Float)
    perstopfee = db.Column(db.Float)
    status = db.Column(db.String(4))
    drivername = db.Column(db.String(32))  # FIXME: Can be removed
    driverphone = db.Column(db.String(16))  # FIXME: Can be removed
    deliverdate = db.Column(db.DateTime)
    finishedtime = db.Column(db.DateTime)

    def __repr__(self):
        return '<Order %r>' % self.oid

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'oid' : self.oid,
            'title' : self.title,
            'pickupaddr' : self.pickupaddr,
            'pickuptime' : self.pickuptime.strftime(DATETIME_FORMAT),
            'did' : self.did,
            'totalcargosize' : self.totalcargosize,
            'trucksize' : self.trucksize,
            'initialfee' : self.initialfee,
            'perstopfee' : self.perstopfee,
            'status' : self.status,
            'drivername' : self.drivername,
            'driverphone' : self.driverphone,
            'deliverdate' : self.deliverdate.strftime(DATETIME_FORMAT),
            'finishedtime' : self.finishedtime.strftime(DATETIME_FORMAT) if self.finishedtime else '',
        }


class OrderRecord(db.Model):
    # orid = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer, primary_key=True)
    did = db.Column(db.Integer)
    stopaddress = db.Column(db.String(128))
    cargosize = db.Column(db.Integer)
    totalfee = db.Column(db.Float)
    status = db.Column(db.String(4))
    grade = db.Column(db.Float)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<OrderRecord %s, %s>' % (self.oid, self.sid)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'oid' : self.oid,
            'sid' : self.sid,
            'did' : self.did,
            'stopaddress' : self.stopaddress,
            'cargosize' : self.cargosize,
            'totalfee' : self.totalfee,
            'status' : self.status,
            'grade' : self.grade,
            'comment' : self.comment
        }

class Shipper(UserMixin, db.Model):
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

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'sid' : self.sid,
            'name' : self.name,
            'passwd' : self.passwd,
            'email' : self.email,
            'phone' : self.phone,
            'addr_1' : self.addr_1,
            'addr_2' : self.addr_2,
            'city' : self.city,
            'state' : self.state,
            'zip' : self.zip,
        }

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

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'did' : self.did,
            'name' : self.name,
            'passwd' : self.passwd,
            'email' : self.email,
            'phone' : self.phone,
            'addr_1' : self.addr_1,
            'addr_2' : self.addr_2,
            'city' : self.city,
            'state' : self.state,
            'zip' : self.zip,
            'grade' : self.grade,
        }
