# -*- coding: utf-8 -*-
"""
Controllers for the app
"""
from theApp import db
from .models import *
from datetime import date, datetime
from werkzeug.security import generate_password_hash


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

    db_session.add(shipper_1)
    db_session.add(shipper_2)
    db_session.add(deliverer_1)
    db_session.add(deliverer_2)

    db_session.commit()
