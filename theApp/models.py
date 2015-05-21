# -*- coding: utf-8 -*-
"""
Models for database of the flask application.
"""

from theApp import app, db
from werkzeug.security import generate_password_hash
from .util import *

# db.session
db_session = db.session


class Order(db.Model):
    oid = db.Column(db.Integer, primary_key=True)  # auto-inc
    pickupaddr = db.Column(db.String(128))
    pickuptime = db.Column(db.DateTime)
    did = db.Column(db.Integer)
    totalcargosize = db.Column(db.Integer)
    trucksize = db.Column(db.Integer)
    totalfee = db.Column(db.Float)
    basefee = db.Column(db.Float)
    closefee = db.Column(db.Float)
    status = db.Column(db.String(4))
    drivername = db.Column(db.String(32))
    driverphone = db.Column(db.String(16))

    def __repr__(self):
        return '<Order %r>' % self.oid

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'oid' : self.oid,
            'pickupaddr' : self.pickupaddr,
            'pickuptime' : self.pickuptime.strftime(DATETIME_FORMAT),
            'did' : self.did,
            'totalcargosize' : self.totalcargosize,
            'trucksize' : self.trucksize,
            'totalfee' : self.totalfee,
            'basefee' : self.basefee,
            'closefee' : self.closefee,
            'status' : self.status,
            'drivername' : self.drivername,
            'driverphone' : self.driverphone
        }


class OrderRecord(db.Model):
    # orid = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.Integer, primary_key=True)
    did = db.Column(db.Integer)
    stopaddress = db.Column(db.String(128))
    delivertime = db.Column(db.DateTime)
    cargosize = db.Column(db.Integer)
    expectfee = db.Column(db.Float)
    fee = db.Column(db.Float)
    acceptedtime = db.Column(db.DateTime) 
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
            'delivertime' : self.delivertime.strftime(DATETIME_FORMAT),
            'cargosize' : self.cargosize,
            'expectfee' : self.expectfee,
            'fee' : self.fee,
            'acceptedtime' : self.acceptedtime.strftime(DATETIME_FORMAT),
            'status' : self.status,
            'grade' : self.grade,
            'comment' : self.comment
        }

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
