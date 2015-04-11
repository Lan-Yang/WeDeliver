# -*- coding: utf-8 -*-
"""
Controllers for the app
"""
from theApp import db
from .models import *

def resetdb():
    db.drop_all()
    db.create_all()
