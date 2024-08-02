#!venv/bin/python

import os
from flask import Flask,request,render_template,redirect,send_file

from junior.pdf import TableContentParser as Parser
from junior.pdf import Runner as runner
from junior.time import getutc,getUtcTextFormat

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/database",methods=["GET"])
def view_database():
	return send_file(os.getcwd()+"/"+fileName+".pdf",as_attachment=True)

@app.route("/submit_datas",methods=["POST"])
def submit_combined():
	if request.method == 'POST':
		vhclid = request.form['vehicle_id']
		item = request.form['item']
		global client
		global fileName
		
		client=request.form['client']
		fileName=str(client)+getUtcTextFormat(6)
		loadwght = request.form['load_weight']
		unloadwght= request.form['unload_weight']
		deduct = request.form['deduct']
		
		net=(int(loadwght)-int(deduct))-int(unloadwght)
		bodys=[vhclid,item,client,getutc(6),loadwght,unloadwght,deduct,str(net)]
		try:
			parser=Parser(fileName)
			parser.putKeysAndValues("Vehicel Id,Item,Client,Time,Load Weight,Unload Weight,Deduct,Net Weight".split(","),bodys)
			parser.parse()
			runner().run(fileName,"P")
			return '<h1>Form submitted successfully</h1>' and send_file(os.getcwd()+"/"+fileName+".pdf",as_attachment=True)
		except Exception as e:
			print(e)
			return '<h1>{{e}}</h1>'
	else:
		return 'Invalid request method'


if __name__ =='__main__':
	app.run(debug=True,host="0.0.0.0")
