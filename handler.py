#-*- coding:utf-8 -*-

from flask import request
from flask import jsonify
from pymongo import MongoClient
import json

client = MongoClient('localhost',27017)
db = client.test
events = db.events

def save_event():
    print('enter save_event data'+request.data)

    data = {
        "name":request.form.get('name', 'name'),
        "avatar":request.form.get('avatar', 'avatar'),
        "timestamp": request.form.get('timestamp', 'timestamp'),
        "msg": request.form.get('msg', 'msg'),
        "location": request.form.get('location', 'location'),
    }
    print(data)

    events.insert(data)
    print('exit save_event')
    return jsonify(code=200, msg='success')

def get_events():
    print('enter get_events')
    datas = events.find({"name":request.args.get('name')})
    array = []
    for info in datas:
        item = {}
        item['name'] = info.get('name')
        item['avatar'] = info.get('avatar')
        item['timestamp'] = info.get('timestamp')
        item['msg'] = info.get('msg')
        item['location'] = info.get('location')

        array.append(item)
        print(item)
    print('exit get_events')
    return jsonify(code=200, msg='success', data=json.dumps(array, ensure_ascii=False))
