# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, flash, redirect, session, url_for, jsonify, send_file
from theApp import app, db, lm, photos
from flask.ext.login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import Environment, Undefined


@app.before_first_request
def init():
    pass

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return "hello world!"
