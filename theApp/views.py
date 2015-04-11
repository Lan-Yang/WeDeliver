# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, flash, redirect, session, url_for, jsonify, send_file
from theApp import app, db, lm, controllers
from flask.ext.login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import Environment, Undefined
from .forms import *


@lm.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.before_first_request
def init():
    pass

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
    	'home.html',
    	title="Home"
    	)

@app.route('/login')
def login():
	return render_template(
		'log.html',
		title="Login"
		)


@app.route('/user/login', methods=['POST'])
def user_login():
    form = LoginForm()
    if not form.validate_on_submit():
        return jsonify(
            status=0,
            message=form.errors.values()[0]  # first error message
        )
    # Login valid form
    login_user(form.user, remember=form.rememberme)
    s = 1 if form.user.get(sid) else 2  # 1 - shipper, 2 - deliverer
    return jsonify(
        status=s
    )


@app.route('/reset/db')
def reset_db():
    controllers.resetdb()
    return "reset db."
