# -*- coding: utf-8 -*-
"""
data API
"""
from theApp import app
from flask import render_template, request, flash, redirect, url_for, jsonify
from .models import *
from sqlalchemy import and_
from .util import *
from datetime import date, datetime


@app.route('/v1/order', methods=['GET'])
def search_for_orders():
    request_args = request.args
    pickupaddress = request_args.get('pickupaddress', '')
    stopaddress = request_args.get('stopaddress', '')
    pickuptime = request_args.get('pickuptime', '')
    cargosize = request_args.get('cargosize', '')
    offset = request_args.get('offset', '')
    limit = request_args.get('limit', '')

    results = Order.query.filter(
        and_(
            Order.pickupaddr==pickupaddress,
            Order.pickuptime<=datetime.strptime(pickuptime, DATETIME_FORMAT),
            Order.trucksize-Order.totalcargosize>=cargosize,
            )).all()

    return jsonify(
        status = 200,
        data = [i.serialize for i in results],
        links = "links"
    )

@app.route('/v1/order/<oid>', methods=['GET'])
def get_order_from_oid(oid):
    if oid=="all":
        orders = Order.query.all()
        return jsonify(
            status = 200,
            data = [i.serialize for i in orders],
        )
    order = Order.query.get(oid)
    return jsonify(
        status = 200,
        data = [order.serialize],
    )

@app.route('/v1/order', methods=['POST'])
def add_new_order():
    data = request.form
    order = Order()
    order.pickupaddr = data.get("pickupaddr", "")
    order.pickuptime = data.get("pickuptime", "")
    order.did = data.get("did", "")
    order.cargosize = data.get("cargosize", "")
    order.trucksize = data.get("trucksize", "")
    order.totalfee = data.get("totalfee", "")
    order.basefee = data.get("basefee", "")
    order.closefee = data.get("closefee", "")
    order.status = data.get("status", "")
    order.drivername = data.get("drivername", "")
    order.driverphone = data.get("driverphone", "")
    db_session.add(order)
    db_session.commit()
    return jsonify(
        status = 201,
        data = "order creation succeeds"
    )