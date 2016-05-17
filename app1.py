# delete.py

from flask import Flask, request, jsonify, render_template, redirect
import json

import md5
	                   
app = Flask(__name__)

user_credentials = {}

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/md5', methods = ['POST'])
def ajax_request():
	key_string = request.form['key_string'] 
	digest_message = md5.new()
	digest_message.update(key_string)
	tmp = digest_message.hexdigest()
	print tmp

	return jsonify(dm=tmp)

@app.route('/register.html', methods = ['GET','POST'])
def register():
	return render_template('register.html')

@app.route('/login.html',methods = ['GET','POST'])
def login():
	return render_template('login.html')

@app.route('/register_end',methods = ['GET', 'POST'])
def register_end():
	code=0
	dataDict = request.data
	dataDict=json.loads(dataDict)
	print dataDict
	if dataDict['username'] not in user_credentials:
		user_credentials[dataDict['username']] = dataDict
		response = "User registered Successfully"
		code =1
		#return redirect('/register_success')
	else:
		response = "Username already taken"
	print response
	return jsonify(response=response,code=code)

@app.route('/login_end',methods = ['GET','POST'])
def login_end():
	code =0
	dataDict = request.data
	dataDict = json.loads(dataDict)
	if dataDict['username'] in user_credentials:
		user = user_credentials[dataDict['username']]
		print dataDict
		if dataDict['password'] == user['password']:	
			response = "Successfully logged in"
			code =1
			return jsonify(response=response,code=code)
		else:
			response = "incorrect password"
	else:
		response = "user doesn't exists"

	print response
	return jsonify(response=response,code=code)

@app.route('/register_success',methods=['GET'])
def register_success():
	return 'successfully registerd'

@app.route('/login_success')
def login_success():
	return 'successfully logged in'


if __name__ == "__main__":
	app.run(debug = True)
