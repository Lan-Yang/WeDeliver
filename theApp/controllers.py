# -*- coding: utf-8 -*-
"""
Controllers for the app
"""
from theApp import db
from .models import *
from datetime import date, datetime


def resetdb():
    db.drop_all()
    db.create_all()

    shipper_1 = Shipper(
        name = "Jack Ma",
        passwd = "123123",
        email = "jackma@hotmail.com",
        phone = "9179112008",
        homeaddr = "181 Claremont Avenue, Apt 2B, New York"
        )

    shipper_2 = Shipper(
        name = "Tom Li",
        passwd = "123123",
        email = "tl2929@columbia.edu",
        phone = "9179132208",
        homeaddr = "i-house Claremont Avenue, Apt 5B, New York"
        )

    deliverer_1 = Deliverer(
        name = "Kuaidi wang",
        passwd = "123123",
        email = "kuaidiw@kuaihua.com",
        phone = "9179133308",
        companyaddr = "Flusing Shildern Garden, Apt 5B, New York",
        grade = 4.3
        )

    deliverer_2 = Deliverer(
        name = "Paul Aho",
        passwd = "123123",
        email = "Ahogo@yahoo.com",
        phone = "9179132222",
        companyaddr = "MailerStreet, W107, New York",
        grade = 3.9
    )

    db_session.add(shipper_1)
    db_session.add(shipper_2)
    db_session.add(deliverer_1)
    db_session.add(deliverer_2)

    db_session.commit()
