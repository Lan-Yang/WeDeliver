# -*- coding: utf-8 -*-
"""
data API
"""
from theApp import app
from flask import request
from .models import *
from sqlalchemy import and_

@app.route('/v1/order', methods=['GET'])
def search_for_orders():
    request_args = request.args
    
    pickupaddress = request_args.get('pickupaddress', '')
    stopaddress = request_args.get('stopaddress', '')
    pickuptime = request_args.get('pickuptime', '')
    cargosize = request_args.get('remainingspace', '')
    offset = request_args.get('offset', '')
    limit = request_args.get('limit', '')

    # results = Order.query.filter(
    #     and_(
    #         Order.pickupaddr==pickupaddress,
    #         Order.pickuptime>=pickuptime,
    #         Order.trucksize-Order.cargosize>=cargosize,
    #         ))
    results = Order.query
    print "query"
    print results.all()
    return "haha"