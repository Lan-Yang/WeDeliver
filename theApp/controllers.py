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

    order = Order(
        pickupaddr='haha',
        pickuptime=datetime.today()
        )
    db_session.add(order)
    db_session.commit()
