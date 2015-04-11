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
    return render_template('home.html')


@app.route('/shipper/login', methods=['POST'])
def shipper_login():
    form = SLoginForm()
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


@app.route('/reset/db')
def reset_db():
    controllers.resetdb()
    return "reset db."
