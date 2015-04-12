# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, flash, redirect, url_for, jsonify
from theApp import app, db, lm, controllers
from flask.ext.login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import Environment, Undefined
from .forms import *


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

@app.route('/s-search')
def ssearch():
	return render_template(
		's-search.html',
		title="ShipperSearch"
		)

@app.route('/s-post')
def spost():
	return render_template(
		's-post.html',
		title="ShipperPost"
		)

@app.route('/s-ongoing')
def songoing():
	return render_template(
		's-ongoing.html',
		title="ShipperOngoing"
		)

@app.route('/account')
def account():
	return render_template(
		'account.html',
		title="Account"
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
    return jsonify(
        status=1
    )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/reset/db')
def reset_db():
    controllers.resetdb()
    return "reset db."
