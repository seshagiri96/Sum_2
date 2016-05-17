# delete.py

from flask import Flask, request, jsonify, render_template, redirect, \
					make_response, session
import json

import md5
	                   
app = Flask(__name__)

user_credentials = {'test':{'username':'test','password':'test','firstname':'test','lastname':'test','biodata':'test'}}
loggedin_users = []

@app.route('/')
def index():
	
	username = request.cookies.get('userId')
	print username,'<--username'
	if username in session:
		return render_template('profile.html',user=user_credentials[username])
	
	return render_template('index.html')

@app.route('/md5', methods = ['POST'])
def ajax_request():
	key_string = request.form['key_string'] 
	digest_message = md5.new()
	digest_message.update(key_string)
	tmp = digest_message.hexdigest()
	print tmp

	return jsonify(dm=tmp)


#----------------------------------------------


@app.route('/register.html', methods = ['GET','POST'])
def register():
	return render_template('register.html')

@app.route('/login.html',methods = ['GET','POST'])
def login():
	return render_template('login.html')


#----------------------------------------------


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
		if dataDict['password'] == user['password']:	
			response = "Successfully logged in"
			loggedin_users.append(dataDict['username'])
			session[dataDict['username']] = dataDict['username']
			print session
			code =1
			response = make_response(jsonify(response=response,code=code,userData=user))
			response.set_cookie('userId',user['username'])
			return response
		else:
			response = "Incorrect password !!"
	else:
		response = "User doesn't exists !!"

	print response
	return jsonify(response=response,code=code)

@app.route('/register_success',methods=['GET'])
def register_success():
	return 'successfully registerd'

@app.route('/profile.html',methods = ['GET','POST'])
def login_success():
	username=request.args.get('username')
		
	if username in session:
		return render_template('profile.html',user=user_credentials[username])
		
	#if username in loggedin_users:
	#	userData = user_credentials[username]
	else:
		print 'redirect'
		return redirect('login.html')
	resp = make_response(render_template('profile.html',user=userData))
	resp.set_cookie('userId',username)

	return resp

@app.route('/logout.html')
def logout():
	username = request.cookies.get('userId')
	session.pop(username,None)
	return render_template('logout.html')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
	app.run(debug = True)
