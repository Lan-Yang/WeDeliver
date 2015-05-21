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
import math


@app.route('/v1/order', methods=['GET'])
def search_for_orders():
    request_args = request.args
    pickupaddress = request_args.get('pickupaddress', '')
    stopaddress = request_args.get('stopaddress', '')
    pickuptime = request_args.get('pickuptime', '')
    cargosize = request_args.get('cargosize', '')
    page_number = request_args.get('page_number', '1')
    per_page = request_args.get('per_page', DEFAULE_PER_PAGE)
    debug = request_args.get('debug', '0')  # for testing, return all records

    results = None

    if debug != '0':
        results = Order.query
        results_pagination = results.paginate(int(page_number), int(per_page), False).items
    else:
        results = Order.query.filter(
            and_(
                Order.pickupaddr==pickupaddress,
                Order.pickuptime<=datetime.strptime(pickuptime, DATETIME_FORMAT),
                Order.trucksize-Order.totalcargosize>=int(cargosize),
                ))
        results_pagination = results.paginate(int(page_number), int(per_page), False).items
    total_count = results.count()
    total_page = int(math.ceil(total_count*1.0/DEFAULE_PER_PAGE))
    first_page_num,last_page_num = 1,total_page
    pre_page_num = int(page_number)-1 if int(page_number)>1 else first_page_num
    next_page_num = int(page_number)+1 if int(page_number)<last_page_num else last_page_num

    return jsonify(
        status = 200,
        data = [i.serialize for i in results_pagination],
        links = [
            {"ref":"pre", "href":"/v1/order?"+"pickupaddress="+pickupaddress+"&stopaddress="+stopaddress+"&pickuptime="+pickuptime+"&cargosize="+cargosize+"&page_number="+str(pre_page_num)+"&per_page="+str(per_page)+"&debug="+debug},
            {"ref":"next","href":"/v1/order?"+"pickupaddress="+pickupaddress+"&stopaddress="+stopaddress+"&pickuptime="+pickuptime+"&cargosize="+cargosize+"&page_number="+str(next_page_num)+"&per_page="+str(per_page)+"&debug="+debug},
            {"ref":"first","href":"/v1/order?"+"pickupaddress="+pickupaddress+"&stopaddress="+stopaddress+"&pickuptime="+pickuptime+"&cargosize="+cargosize+"&page_number="+str(first_page_num)+"&per_page="+str(per_page)+"&debug="+debug},
            {"ref":"last","href":"/v1/order?"+"pickupaddress="+pickupaddress+"&stopaddress="+stopaddress+"&pickuptime="+pickuptime+"&cargosize="+cargosize+"&page_number="+str(last_page_num)+"&per_page="+str(per_page)+"&debug="+debug},
            ]
    )

@app.route('/v1/order/<oid>', methods=['GET'])
def get_order_from_oid(oid):
    if oid=="all":  # used for test
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
    order.did = data.get("did", "0")
    order.cargosize = data.get("cargosize", "0")
    order.trucksize = data.get("trucksize", "0")
    order.totalfee = data.get("totalfee", "0")
    order.basefee = data.get("basefee", "0")
    order.closefee = data.get("closefee", "0")
    order.status = data.get("status", "O")
    order.drivername = data.get("drivername", "")
    order.driverphone = data.get("driverphone", "")
    db_session.add(order)
    db_session.commit()
    return jsonify(
        status = 201,
        data = "order creation succeeds"
    )

@app.route('/v1/orderRecord', methods=['GET'])
def search_for_orderRecords_from_sid():
    request_args = request.args
    sid = request_args.get('sid', '')
    page_number = request_args.get('page_number', '1')
    per_page = request_args.get('per_page', DEFAULE_PER_PAGE)

    results = OrderRecord.query.filter(
            OrderRecord.sid == sid
        )
    results_pagination = results.paginate(int(page_number), int(per_page), False).items

    total_count = results.count()
    total_page = int(math.ceil(total_count*1.0/DEFAULE_PER_PAGE))
    first_page_num,last_page_num = 1,total_page
    pre_page_num = int(page_number)-1 if int(page_number)>1 else first_page_num
    next_page_num = int(page_number)+1 if int(page_number)<last_page_num else last_page_num

    return jsonify(
        status = 200,
        data = [i.serialize for i in results_pagination],
        links = [
            {"ref":"pre", "href":"/v1/orderRecord?"+"sid="+sid+"&page_number="+str(pre_page_num)+"&per_page="+str(per_page)},
            {"ref":"next","href":"/v1/orderRecord?"+"sid="+sid+"&page_number="+str(next_page_num)+"&per_page="+str(per_page)},
            {"ref":"first","href":"/v1/orderRecord?"+"sid="+sid+"&page_number="+str(first_page_num)+"&per_page="+str(per_page)},
            {"ref":"last","href":"/v1/orderRecord?"+"sid="+sid+"&page_number="+str(last_page_num)+"&per_page="+str(per_page)},
            ]
    )

@app.route('/v1/orderRecord/all', methods=['GET'])  # used for test
def get_orderRecords():
    orders = OrderRecord.query.all()
    return jsonify(
        status = 200,
        data = [i.serialize for i in orders],
    )

@app.route('/v1/orderRecord', methods=['POST'])
def add_new_orderRecord():
    data = request.form
    orderRecord = OrderRecord()
    orderRecord.oid = data.get("oid", "")
    orderRecord.sid = data.get("sid", "")
    orderRecord.did = data.get("did", "")
    orderRecord.stopaddress = data.get("stopaddress", "")
    orderRecord.delivertime = data.get("delivertime", "")
    orderRecord.cargosize = data.get("cargosize", "")
    orderRecord.expectfee = data.get("expectfee", "")
    orderRecord.fee = data.get("fee", "")
    orderRecord.acceptedtime = data.get("acceptedtime", "")
    orderRecord.status = data.get("status", "")
    orderRecord.grade = data.get("grade", "")
    orderRecord.comment = data.get("comment", "")
    db_session.add(orderRecord)
    db_session.commit()
    return jsonify(
        status = 201,
        data = "orderRecord creation succeeds"
    )

@app.route('/v1/shipper/<sid>', methods=['GET'])
def get_shipper_profile(sid):
    shipper = Shipper.query.get(sid)
    if shipper:  # if found
        shipper_data = shipper.serialize
        shipping_history = get_shipping_history(sid)
        shipper_data['shipping_history'] = shipping_history
        shipper_data['shipper_total_delivers'] = get_shipper_total_delivers(shipping_history)
        shipper_data['shipper_total_savings'] = get_shipper_total_savings(shipping_history)
        shipper_data['shipper_credits'] = get_shipper_credits(shipping_history)
        return jsonify(
            status = 200,
            data = [shipper_data],
        )
    else:  # not found
        return jsonify(
            status = 404,
            data = "shipper not found"
        )

def get_shipper_total_delivers(shipping_history):
    return len(shipping_history)

def get_shipper_total_savings(shipping_history):
    total_savings = 0
    for sh in shipping_history:
        total_savings += sh["you_save"]
    return total_savings

def get_shipper_credits(shipping_history):
    shipper_credits = 0
    for sh in shipping_history:
        shipper_credits += sh["actual_pay"]

def get_totalfee_from_oid(oid):
    shipper_order = Order.query.get(oid)
    return shipper_order.totalfee

def get_shipper_complete_order_records(sid):
    return OrderRecord.query.filter(
        and_(
            OrderRecord.sid == sid,
            OrderRecord.status == "F"
        ))

def get_shipping_history(sid):
    shipper_complete_order_records = get_shipper_complete_order_records(sid)
    shipping_history = []
    for orderRecord in shipper_complete_order_records:
        actual_pay = orderRecord.fee
        expected_pay = get_totalfee_from_oid(orderRecord.oid)
        record = {
            "order_record_date": orderRecord.acceptedtime.strftime(DATETIME_FORMAT),
            "actual_pay": actual_pay,
            "expected_pay": expected_pay,
            "you_save": expected_pay-actual_pay
        }
        shipping_history.append(record)
    return shipping_history
