from flask import Flask, render_template, redirect

app = Flask(__name__,template_folder='.')

@app.route('/')
def test():
	return render_template('login.html')

@app.route('/index.html')
def login_end():
	print 'hello'
	return make_response(redirect('register.html'))

app.run()