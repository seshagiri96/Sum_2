# delete.py

from flask import Flask, request, jsonify, render_template 

import md5
	                   
app = Flask(__name__)

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
    
if __name__ == "__main__":
    app.run(debug = True)
