from . import BData
from flask import request, json
from App.BigData.scheduler import *


@BData.route('/insertBigData/', methods = ["GET", "POST"])
def insertBGDT():
	if request.method == "GET":
		pass
	elif request.method == "POST":
		data = request.json
		shce = Sche()
		message = shce.insertBGDT(data)
		return json.dumps(message)


@BData.route('/queryBigData/', methods = ["GET", "POST"])
def queryBigData():
	if request.method == "GET":
		pass
	elif request.method == "POST":
		data = request.json
		shce = Sche()
		if data:
			message = shce.queryALLBGDT(data)
		else:
			message = shce.queryALLBGDT()
		return json.dumps(message)


@BData.route('/queryALLBigData/', methods = ["GET", "POST"])
def queryALLBigData():
	if request.method == "POST":
		data = request.json
		shce = Sche()
		if data:
			message = shce.queryALLBGDT(data)
		else:
			message = shce.queryALLBGDT()
		return json.dumps(message)

@BData.route("/updataBigData/", methods = ["GET", "POST"])
def updataBigData():
	if request.method == "GET":
		return '123'
	elif request.method == "POST":
		data = request.json
		print(data)
		sche = Sche()
		message = sche.updataBigData(data)
		return json.dumps(message)


@BData.route("/deleteBigData/", methods = ["GET", "POST"])
def deleteBigData():
	if request.method == "GET":
		pass
	elif request.method == "POST":
		data = request.json
		sche = Sche()
		print(data)
		message = sche.deleteBigData(data)
		return json.dumps(message)
