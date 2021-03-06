# -*- coding: utf-8 -*-
"""
data API
"""
from theApp import app, ses
from flask import render_template, request, flash, redirect, url_for, jsonify
from .models import *
from sqlalchemy import and_, desc, update
from .util import *
from datetime import date, datetime
import math


@app.route('/v1/order', methods=['GET'])
def search_for_orders1():
    request_args = request.args
    pickupaddress = request_args.get('pickupaddress', '')
    stopaddress = request_args.get('stopaddress', '')
    pickuptime = request_args.get('pickuptime', '')
    cargosize = request_args.get('cargosize', 0)
    status = request_args.get('status', '')  # NEW, single status query
    page_number = request_args.get('page_number', '1')
    per_page = request_args.get('per_page', DEFAULE_PER_PAGE)
    debug = request_args.get('debug', '0')  # for testing, return all records

    results = None

    if debug != '0':
        results = Order.query.filter(Order.status==status).order_by(desc(Order.oid))
    else:
        results = Order.query.filter(
            and_(
                Order.pickupaddr==pickupaddress,
                # Order.pickuptime<=datetime.strptime(pickuptime, DATETIME_FORMAT),
                Order.trucksize-Order.totalcargosize>=int(cargosize),
                )).order_by(desc(Order.oid))
    results_pagination = results.paginate(int(page_number), int(per_page), False).items
    total_count = results.count()
    total_page = int(math.ceil(total_count*1.0/DEFAULE_PER_PAGE))
    first_page_num,last_page_num = 1,total_page
    pre_page_num = int(page_number)-1 if int(page_number)>1 else first_page_num
    next_page_num = int(page_number)+1 if int(page_number)<last_page_num else last_page_num

    result = [i.serialize for i in results_pagination]
    # Join deliverer table
    for order in result:
        try:
            deliverer = Deliverer.query.get(order['did'])
        except:
            deliverer = None
        if deliverer:
            order.update({
                'deliverer_name': deliverer.name,
                'deliverer_grade': deliverer.grade
            });
    # Join OrderRecord table
    for order in result:
        try:
            record = OrderRecord.query.filter(OrderRecord.oid == order['oid']).first()
        except:
            record = None
        if record:
            order.update({
                'deliverloc': record.stopaddress,
            });

    PAGELINK = "/v1/order?pickupaddress=%s&stopaddress=%s&pickuptime=%s&cargosize=%s&page_number=%s&per_page=%s&debug=%s"

    return jsonify(
        status = 200,
        data = result,
        links = [
            {"ref":"pre", "href":PAGELINK % (pickupaddress, stopaddress, pickuptime, cargosize, pre_page_num, per_page, debug)},
            {"ref":"next", "href":PAGELINK % (pickupaddress, stopaddress, pickuptime, cargosize, next_page_num, per_page, debug)},
            {"ref":"first", "href":PAGELINK % (pickupaddress, stopaddress, pickuptime, cargosize, first_page_num, per_page, debug)},
            {"ref":"last", "href":PAGELINK % (pickupaddress, stopaddress, pickuptime, cargosize, last_page_num, per_page, debug)},
            # {"ref":"pre", "href":"/v1/order?"+"pickupaddress="+pickupaddress+"&stopaddress="+stopaddress+"&pickuptime="+pickuptime+"&cargosize="+cargosize+"&page_number="+str(pre_page_num)+"&per_page="+str(per_page)+"&debug="+debug},
            # {"ref":"next","href":"/v1/order?"+"pickupaddress="+pickupaddress+"&stopaddress="+stopaddress+"&pickuptime="+pickuptime+"&cargosize="+cargosize+"&page_number="+str(next_page_num)+"&per_page="+str(per_page)+"&debug="+debug},
            # {"ref":"first","href":"/v1/order?"+"pickupaddress="+pickupaddress+"&stopaddress="+stopaddress+"&pickuptime="+pickuptime+"&cargosize="+cargosize+"&page_number="+str(first_page_num)+"&per_page="+str(per_page)+"&debug="+debug},
            # {"ref":"last","href":"/v1/order?"+"pickupaddress="+pickupaddress+"&stopaddress="+stopaddress+"&pickuptime="+pickuptime+"&cargosize="+cargosize+"&page_number="+str(last_page_num)+"&per_page="+str(per_page)+"&debug="+debug},
        ]
    )

@app.route('/v1/order/did/<did>/status/<status>', methods=['GET'])
@app.route('/v1/order/did/<did>/status', methods=['GET'])
@app.route('/v1/order/did/<did>', methods=['GET'])
def search_for_orders2(did, status=""):
    status_list = None
    if status:
        status_list = status.split(",")
    results = Order.query.filter(
            Order.did == did,
        )
    if status_list:
        results = [order for order in results if order.status in status_list]
    return jsonify(
        status = 200,
        data = [i.serialize for i in results]
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
    result = order.serialize
    odrds = OrderRecord.query.filter(
            OrderRecord.oid == oid
        )
    orderRecords = []
    for odrd in odrds:
        orderRecords.append(odrd.serialize)
    try:
        deliverer = Deliverer.query.get(order.did)
    except:
        deliverer = None
    result["orderRecords"] = orderRecords
    result["deliverer_name"] = deliverer and deliverer.name
    result["deliverer_grade"] = deliverer and deliverer.grade
    return jsonify(
        status = 200,
        data = [result],
    )

@app.route('/v1/order', methods=['POST'])
def add_new_order():
    data = request.form
    order = Order()
    order.title = data.get("title", "IKEA GO")  # NEW
    order.pickupaddr = data.get("pickupaddr", "IKEA Brooklyn")
    order.pickuptime = data.get("pickuptime", None)
    order.did = data.get("did", 0)
    order.trucksize = data.get("trucksize", 0)
    order.initialfee = data.get("initialfee", 0)
    order.perstopfee = data.get("perstopfee", 10)  # default 10
    order.status = data.get("status", "O")
    order.drivername = data.get("drivername", "xxyy")
    order.driverphone = data.get("driverphone", "123456")
    order.deliverdate = data.get("deliverdate", None)
    # order.finishedtime = data.get("finishedtime", "")  # KEEP NULL
    order.pickupaddr_lat = data.get("pickupaddr_lat", 0)
    order.pickupaddr_lng = data.get("pickupaddr_lng", 0)
    order.totalcargosize = 0
    order.participants = 0
    db_session.add(order)
    db_session.commit()
    try:
        oid = order.oid
    except Exception as e:
        oid = Order.query.count()
    return jsonify(
        status = 201,
        data = "order creation succeeds",
        oid = oid,  # NEW
    )

@app.route('/v1/order/<oid>', methods=['PUT'])
def update_order(oid):
    request_args = request.form
    this_order = Order.query.get(oid)
    for key in request_args:
        # print key
        setattr(this_order, key, request_args[key])
    db_session.commit()
    return jsonify(
        status = 200,
        data = "update succeeds",
        oid = oid
    )

@app.route('/v1/orderRecord', methods=['GET'])
def search_for_orderRecords_from_sid_and_status():
    request_args = request.args
    sid = request_args.get('sid', '')
    if not sid:
        return jsonify(
                status = 400,
                data = "no sid provided"
            )
    status = request_args.get('status', '')
    page_number = request_args.get('page_number', 1)
    per_page = request_args.get('per_page', DEFAULE_PER_PAGE)

    status_list = None
    if status:
        status_list = status.split(',')

    odrds = OrderRecord.query.filter(
        OrderRecord.sid == sid
    )
    results = []
    for odrd in odrds:
        # print odrd.oid
        # print type(odrd.oid), odrd.oid
        oid = odrd.oid
        this_order = Order.query.get(oid)
        if not status_list or this_order.status in status_list:
            odrd_dict = odrd.serialize
            odrd_dict.update(this_order.serialize)
            results.append(odrd_dict)
    # results = OrderRecord.query \
    #     .join(Order, OrderRecord.oid==Order.oid) \
    #     .add_columns(Order.title, Order.pickupaddr, Order.pickuptime, Order.did, Order.totalcargosize, Order.trucksize, Order.initialfee, Order.perstopfee, Order.status, Order.drivername, Order.driverphone, Order.deliverdate, Order.finishedtime, Order.pickupaddr_lat, Order.pickupaddr_lng, Order.participants) \
    #     .filter(
    #         OrderRecord.sid == sid,
    #     )
    # if status_list:
    #     results = [order for order in results if order.status in status_list]

    # results_pagination = results.paginate(int(page_number), int(per_page), False).items

    # total_count = results.count()
    # total_page = int(math.ceil(total_count*1.0/DEFAULE_PER_PAGE))
    # first_page_num,last_page_num = 1,total_page
    # pre_page_num = int(page_number)-1 if int(page_number)>1 else first_page_num
    # next_page_num = int(page_number)+1 if int(page_number)<last_page_num else last_page_num

    return jsonify(
        status = 200,
        data = results,
        # links = [
        #     {"ref":"pre", "href":"/v1/orderRecord?"+"sid="+sid+"&page_number="+str(pre_page_num)+"&per_page="+str(per_page)},
        #     {"ref":"next","href":"/v1/orderRecord?"+"sid="+sid+"&page_number="+str(next_page_num)+"&per_page="+str(per_page)},
        #     {"ref":"first","href":"/v1/orderRecord?"+"sid="+sid+"&page_number="+str(first_page_num)+"&per_page="+str(per_page)},
        #     {"ref":"last","href":"/v1/orderRecord?"+"sid="+sid+"&page_number="+str(last_page_num)+"&per_page="+str(per_page)},
        #     ]
    )

@app.route('/v1/orderRecord/<oid>/<sid>', methods=['GET'])
@app.route('/v1/orderRecord/all', methods=['GET'])  # used for test
def get_orderRecords(oid=None, sid=None):
    if not oid and not sid:
        orderRecords = OrderRecord.query.all()
    else:
        orderRecords = OrderRecord.query.filter(
        and_(
            OrderRecord.oid == oid,
            OrderRecord.sid == sid
            )
        )
    return jsonify(
        status = 200,
        data = [i.serialize for i in orderRecords],
    )

@app.route('/v1/orderRecord', methods=['POST'])
def add_new_orderRecord():
    data = request.form
    try:
        orderRecord = OrderRecord()
        orderRecord.oid = data.get("oid", 0)
        orderRecord.sid = data.get("sid", 0)
        orderRecord.stopaddress = data.get("stopaddress", "")
        orderRecord.cargosize = data.get("cargosize", 5)
        orderRecord.totalfee = data.get("totalfee", 0)
        # orderRecord.status = data.get("status", "")
        orderRecord.grade = data.get("grade", 0)
        orderRecord.comment = data.get("comment", "")
        orderRecord.stopaddr_lat = data.get("stopaddr_lat", 0)
        orderRecord.stopaddr_lng = data.get("stopaddr_lng", 0)
        db_session.add(orderRecord)
        db_session.commit()

        this_order = Order.query.get(orderRecord.oid)
        this_order.participants += 1  # update order participants
        this_order.totalcargosize += int(orderRecord.cargosize)
        db_session.commit()

        return jsonify(
            status = 201,
            data = "orderRecord creation succeeds"
        )
    except Exception as e:
        return jsonify(
            status = 201,
            data = "%r" % e,
        )

@app.route('/v1/orderRecord/<oid>/<sid>', methods=['PUT'])
def update_orderRecord(oid, sid):
    request_args = request.form
    this_OrderRecord = OrderRecord.query.filter(
        and_(
            OrderRecord.oid == oid,
            OrderRecord.sid == sid
            )
        ).first()
    for key in request_args:
        # print key
        setattr(this_OrderRecord, key, request_args[key])
    db_session.commit()
    return jsonify(
        status = 200,
        data = "update succeeds",
        oid = oid,
        sid = sid
    )


def get_shipper_profile_(sid):
    shipper = Shipper.query.get(sid)
    if not shipper:  # if not found
        return None
    shipper_data = shipper.serialize
    shipping_history = get_shipping_history(sid)
    shipper_data['shipping_history'] = shipping_history
    shipper_data['shipper_total_delivers'] = get_shipper_total_delivers(shipping_history)
    shipper_data['shipper_total_savings'] = get_shipper_total_savings(shipping_history)
    shipper_data['shipper_credits'] = get_shipper_credits(shipping_history)
    return shipper_data


@app.route('/v1/shipper/<sid>', methods=['GET'])
def get_shipper_profile(sid):
    shipper_data = get_shipper_profile_(sid)
    if shipper_data:  # if found
        return jsonify(
            status = 200,
            data = [shipper_data],
        )
    else:  # not found
        return jsonify(
            status = 404,
            data = "shipper not found"
        )

# def get_deliverer_profile_(did):
    # deliverer = Deliverer.query.get(did)
    # if not deliverer:
    #     return None
#     deliverer_data = deliverer.serialize
#     # delivering_history = get_delivering_history(did)
#     # deliverer_data['delivering_history'] = delivering_history
#     deliverer_data['deliverer_total_delivers'] = get_deliverer_total_delivers(did)
#     deliverer_data['deliverer_total_savings'] = get_deliverer_total_savings(did)
#     deliverer_data['deliverer_credits'] = get_shipper_credits(did)
#     return deliverer_data


@app.route('/v1/deliverer/<did>', methods=['GET'])
def get_deliverer_profile(did):
    deliverer = Deliverer.query.get(did)
    if not deliverer:
        return jsonify(
            status = 404,
            data = "deliverer not found"
        )
    else:
        return jsonify(
            status = 200,
            data = [deliverer.serialize]
        )


@app.route('/v1/mailto/<sid>', methods=["POST"])
def mail_to_sid(sid):
    request_args = request.form
    shipper = Shipper.query.get(int(sid))
    if not shipper:
        return jsonify(
            status=404,
            data="no such shipper",
        )
    title = request_args.get("title", "Email from WeDeliver")
    body = request_args.get("body", "This is an email from WeDeliver")
    recipient = shipper.email
    try:
        ses.send_email(
            app.config['SES_SENDER_EMAIL'],
            title, body, [recipient])
        # print "success"
        return jsonify(
            status=200,
            data="success",
        )
    except Exception as e:
        # print "fail: %r" % e
        return jsonify(
            status=500,
            data="fail: %r" % e,
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

def get_initialfee_from_oid(oid):
    shipper_order = Order.query.get(oid)
    return shipper_order.initialfee

def get_shipper_complete_order_records(sid):
    return OrderRecord.query.filter(
        and_(
            OrderRecord.sid == sid,
            # OrderRecord.status == "F"
        ))

def get_shipping_history(sid):
    shipper_complete_order_records = get_shipper_complete_order_records(sid)
    shipping_history = []
    for orderRecord in shipper_complete_order_records:
        actual_pay = orderRecord.totalfee
        expected_pay = get_initialfee_from_oid(orderRecord.oid)
        record = {
            # "order_record_date": orderRecord.deliverdate.strftime(DATETIME_FORMAT),
            "actual_pay": actual_pay,
            "expected_pay": expected_pay,
            "you_save": expected_pay-actual_pay
        }
        shipping_history.append(record)
    return shipping_history

# def get_deliverer_complete_orders(sid):
#     return Order.query.filter(
#         and_(
#             Order.sid == did,
#             Order.status == "F"
#         ))

# def get_delivering_history(did):
#     deliverer_complete_orders = get_deliverer_complete_orders(sid)
#     delivering_history = []
#     for order in deliverer_complete_orders:


# def get_deliverer_total_delivers(did):
#     deliverer_complete_orders = get_deliverer_complete_orders(sid)