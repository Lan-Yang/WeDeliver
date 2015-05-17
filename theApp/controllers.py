# -*- coding: utf-8 -*-
"""
Controllers for the app
"""
from flask import session
from theApp import app, lm, db
from .models import *
from datetime import date, datetime
from werkzeug.security import generate_password_hash
from flask.ext.login import user_logged_in, user_logged_out
from .util import *


def when_user_logged_in(sender, user, **extra):
    session['shipper_or_deliverer'] = 1 if hasattr(user, 'sid') else 2
    # print "user_logged_in, %s" % session['shipper_or_deliverer']
    session.modified = True

def when_user_logged_out(sender, user, **extra):
    del session['shipper_or_deliverer']
    session.modified = True

user_logged_in.connect(when_user_logged_in, app)
user_logged_out.connect(when_user_logged_out, app)


@lm.user_loader
def load_user(user_id):
    if session.get('shipper_or_deliverer') == 1:
        return Shipper.query.get(int(user_id))
    elif session.get('shipper_or_deliverer') == 2:
        return Deliverer.query.get(int(user_id))
    else:
        return None

def resetdb():
    db.drop_all()
    db.create_all()

    shipper_1 = Shipper()
    shipper_1.name = "Jack Ma"
    shipper_1.passwd = generate_password_hash("123123")
    shipper_1.email = "jackma@hotmail.com"
    shipper_1.phone = "9179112008"
    shipper_1.addr_1 = "181 Claremont Avenue, Apt 2B"
    shipper_1.addr_2 = ""
    shipper_1.city = "New York"
    shipper_1.state = "NY"
    shipper_1.zip = "10027"


    shipper_2 = Shipper()
    shipper_2.name = "Tom Li"
    shipper_2.passwd = generate_password_hash("123123")
    shipper_2.email = "tl2929@columbia.edu"
    shipper_2.phone = "9179112000"
    shipper_2.addr_1 = "i-house Claremont Avenue"
    shipper_2.addr_2 = "Apt 5B"
    shipper_2.city = "New York"
    shipper_2.state = "NY"
    shipper_2.zip = "10027"


    deliverer_1 = Deliverer()
    deliverer_1.name = "Kuaidi wang"
    deliverer_1.passwd = generate_password_hash("123123")
    deliverer_1.email = "kuaidiw@kuaihua.com"
    deliverer_1.phone = "9179133308"
    deliverer_1.addr_1 = "Flusing Shildern Garden"
    deliverer_1.addr_2 = "Apt 5B"
    deliverer_1.city = "New York"
    deliverer_1.state = "NY"
    deliverer_1.zip = "10022"
    deliverer_1.grade = 4.3


    deliverer_2 = Deliverer()
    deliverer_2.name = "Paul Aho"
    deliverer_2.passwd = generate_password_hash("123123")
    deliverer_2.email = "Ahogo@yahoo.com"
    deliverer_2.phone = "9179132222"
    deliverer_2.addr_1 = "MailerStreet W107"
    deliverer_2.addr_2 = ""
    deliverer_2.city = "New York"
    deliverer_2.state = "NY"
    deliverer_2.zip = "10010"
    deliverer_2.grade = 3.9

    order_1 = Order()
    order_1.pickupaddr = "Columbia"
    order_1.pickuptime = datetime.strptime('2011-11-03 18:21:26', DATETIME_FORMAT)
    order_1.did = 1
    order_1.totalcargosize = 3
    order_1.trucksize = 33
    order_1.totalfee = 35.5
    order_1.basefee = 35.5
    order_1.closefee = 35.5
    order_1.status = "D"
    order_1.drivername = "XiDaDa"
    order_1.driverphone = "821931"

    order_2 = Order()
    order_2.pickupaddr = "NYU"
    order_2.pickuptime = datetime.strptime('2011-11-03 18:21:26', DATETIME_FORMAT)
    order_2.did = 1
    order_2.totalcargosize = 3
    order_2.trucksize = 33
    order_2.totalfee = 35.5
    order_2.basefee = 35.5
    order_2.closefee = 35.5
    order_2.status = "D"
    order_2.drivername = "XiDaDa"
    order_2.driverphone = "821931"

    order_3 = Order()
    order_3.pickupaddr = "hahaha"
    order_3.pickuptime = datetime.strptime('2011-11-03 18:21:26', DATETIME_FORMAT)
    order_3.did = 1
    order_3.totalcargosize = 5
    order_3.trucksize = 33
    order_3.totalfee = 35.5
    order_3.basefee = 35.5
    order_3.closefee = 35.5
    order_3.status = "D"
    order_3.drivername = "XiDaDa"
    order_3.driverphone = "821931"

    order_4 = Order()
    order_4.pickupaddr = "hahaha"
    order_4.pickuptime = datetime.strptime('2011-11-03 18:21:26', DATETIME_FORMAT)
    order_4.did = 1
    order_4.totalcargosize = 5
    order_4.trucksize = 33
    order_4.totalfee = 35.5
    order_4.basefee = 35.5
    order_4.closefee = 35.5
    order_4.status = "D"
    order_4.drivername = "XiDaDa"
    order_4.driverphone = "821931"

    order_5 = Order()
    order_5.pickupaddr = "hahaha"
    order_5.pickuptime = datetime.strptime('2011-11-03 18:21:26', DATETIME_FORMAT)
    order_5.did = 1
    order_5.totalcargosize = 5
    order_5.trucksize = 33
    order_5.totalfee = 35.5
    order_5.basefee = 35.5
    order_5.closefee = 35.5
    order_5.status = "D"
    order_5.drivername = "XiDaDa"
    order_5.driverphone = "821931"

    order_6 = Order()
    order_6.pickupaddr = "hahaha"
    order_6.pickuptime = datetime.strptime('2011-11-03 18:21:26', DATETIME_FORMAT)
    order_6.did = 1
    order_6.totalcargosize = 5
    order_6.trucksize = 33
    order_6.totalfee = 35.5
    order_6.basefee = 35.5
    order_6.closefee = 35.5
    order_6.status = "D"
    order_6.drivername = "XiDaDa"
    order_6.driverphone = "821931"

    orderRecord_1 = OrderRecord()
    orderRecord_1.oid = 1
    orderRecord_1.sid = 1
    orderRecord_1.did = 1
    orderRecord_1.stopaddress = "NYU"
    orderRecord_1.delivertime = datetime.strptime('2011-11-03 18:21:26', DATETIME_FORMAT)
    orderRecord_1.cargosize = 33
    orderRecord_1.expectfee = 35.5
    orderRecord_1.fee = 33.3
    orderRecord_1.acceptedtime = datetime.strptime('2011-11-03 18:21:26', DATETIME_FORMAT)
    orderRecord_1.status = "D"
    orderRecord_1.grade = 3.5
    orderRecord_1.comment = "This is great!"

    db_session.add(shipper_1)
    db_session.add(shipper_2)
    db_session.add(deliverer_1)
    db_session.add(deliverer_2)
    db_session.add(order_1)
    db_session.add(order_2)
    db_session.add(order_3)
    db_session.add(order_4)
    db_session.add(order_5)
    db_session.add(order_6)
    db_session.add(orderRecord_1)

    db_session.commit()
