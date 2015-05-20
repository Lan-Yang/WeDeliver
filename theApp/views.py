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
        'index-login.html',
        title="Home"
        )

@app.route('/loginmodal')
def login():
    return render_template(
        'login-modal.html',
        title="Login"
        )

@app.route('/placemodal')
def placemodal():
    return render_template(
        'place-modal.html',
        title="Login"
        )

@app.route('/s-search')
def ssearch():
    return render_template(
        'searchlist-header.html',
        title="ShipperSearch"
        )

@app.route('/s-post')
def spost():
    return render_template(
        'post-header.html',
        title="ShipperPost"
        )

@app.route('/handle_shipper_post', methods=['POST'])
def handle_shipper_post():
    form = ShipperPostForm()
    if not form.validate_on_submit():
        return "the format of submitted form is not right"
    form.recordPost()
    return "Successfully post."

@app.route('/searchlist')  # test search_list.html
def searchlist():
    return render_template(
        'search_list.html',
        # title="ShipperSearch"
        )

@app.route('/s-ongoing')
def songoing():
    return render_template(
        's-ongoing.html',
        title="ShipperOngoing"
        )

@app.route('/s-account')
def account():
    return render_template(
        'profile-header.html',
        title="Account"
        )

@app.route('/order')
def view_order():
    oid = request.args.get("oid")
    return render_template(
        'order.html',
        title="Order Details",
        oid=oid,
        )

@app.route('/myorder')
def list_orders():
    return render_template(
        'shipper_orders.html',
        title="My orders",
        )



@app.route('/user/login', methods=['POST'])
def user_login():
    form = LoginForm()
    if not form.validate_on_submit():
        return jsonify(
            status=0,
            errors=form.errors  # first error message
        )
    # Login valid form
    login_user(form.user, remember=form.rememberme)
    return jsonify(
        status=1
    )

@app.route('/shipper/search', methods=['POST'])
def shipper_search():
    form = SSearchForm()
    if not form.validate_on_submit():
        return jsonify(
            status=0,
            message=form.errors.values()[0]  # first error message
        )
    form.search()
    return jsonify(
        status=1,
        results=form.orders
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
