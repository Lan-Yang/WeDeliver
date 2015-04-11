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

@app.route('/reset/db')
def reset_db():
	controllers.resetdb()
	return "reset db."
