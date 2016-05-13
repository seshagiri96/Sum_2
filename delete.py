 #       variable like I have, I just wanted to keep everything in one
#       file for the sake of completeness of answer.
#       It's generally a very bad way to do things :)
#
from flask import Flask, request, jsonify,render_template 

import md5
	                   
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = request.form['username'] 
    m = md5.new()
    m.update(username) 
    tmp = m.hexdigest()
    print tmp
    

    return jsonify(username=tmp,show_button=False)
    
if __name__ == "__main__":
    app.run(debug = True)
