# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, flash, redirect, url_for, jsonify
from theApp import app, db, lm, controllers
from flask.ext.login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import Environment, Undefined
from .forms import *
from .oauth import OAuthSignIn
from .models import *
from .util import *


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
    # oid = request.args.get("oid")
    return render_template(
        'search-order-detail.html',
        title="Order Details",
        )

@app.route('/myorder')
def list_orders():
    return render_template(
        'shipper_orders.html',
        title="My orders",
        )


@app.route('/search_order_detail')
def list_search_order_detail():
    return render_template(
        'search-order-detail.html',
        title="Order Detail",
        )


@app.route('/rate_order')
def rate_order():
    return render_template(
        'rate_order.html',
        title="Rate My Order",
        )






@app.route('/test/email')
def test_ses():
    title = "We Deliver Email Test"
    body = "This is a test email, send by We Deliver 2015."
    recipients = ["mw2972@columbia.edu", "ly2331@columbia.edu", "jy2653@columbia.edu"]
    controllers.sendmail(title, body, recipients)
    return "Email send to %r" % recipients

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

@app.route('/<user_type>/authorize/<provider>')
def oauth_authorize(user_type, provider):
    if user_type!="shipper" and user_type!="deliverer":
        return jsonify("invalid user type!")
    if not current_user.is_anonymous():
        return redirect(url_for('home'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize(user_type)

@app.route('/<user_type>/callback/<provider>')
def oauth_callback(user_type, provider):
    if not current_user.is_anonymous():
        return redirect(url_for('home'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback(user_type)
    # print social_id, username, email
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('home'))
    new_id = djb2_string_hash(social_id)  ## social_id may contain letters. use djb2 to convert to int
    print new_id
    if user_type=="shipper":
        shipper = Shipper.query.get(new_id)
        if not shipper:
            shipper = Shipper(sid=new_id, name=username, email=email)
            db_session.add(shipper)
            db_session.commit()
        # print 171
        login_user(shipper)
        re_url = url_for('home')
    else:  # deliverer
        deliverer = Deliverer.query.get(new_id)
        if not deliverer:
            deliverer = Deliverer(did=new_id, name=username, email=email)
            db_session.add(deliverer)
            db_session.commit()
        login_user(deliverer)
        re_url = url_for('d_home')
    # print 180
    return redirect(re_url)

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

@app.route('/d-home')
def d_home():
    """Renders the home page."""
    return render_template(
        'd-index-login.html',
        title="Home"
        )

@app.route('/d-loginmodal')
def d_login():
    return render_template(
        'd-login-modal.html',
        title="Login"
        )

@app.route('/d-search')
def d_search():
    return render_template(
        'd-searchlist.html',
        title="DelivererSearch"
        )


@app.route('/d-accept-order')
def d_accept():
    return render_template(
        'accept-order.html',
        title="Accpet Order"
        )

@app.route('/d-myorder')
def d_list_orders():
    return render_template(
        'deliverer_orders.html',
        title="My orders",
        )
@app.route('/d-post')
def d_post():
    return render_template(
        'd-post-header.html',
        title="DelivererPost"
        )
