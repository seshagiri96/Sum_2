var express = require('express');
var cookieParser = require('cookie-parser');
var app = express();

var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('/home/devloper/sessions.db');

app.use(cookieParser());

var requestTime = function (req, res, next) {
  req.requestTim = Date.now();
  next();
};

app.use(requestTime);

app.get('/',function(req,res){
	res.set('Content-Type', 'application/json');
	res.send(JSON.stringify({'response':'Welcom to node server'}));
});

fun = function (req, res) {

	res.set('Content-Type', 'application/json');
	var responseText='';
	try{
		sess = req.cookies.myssid;
		db.all("SELECT * from sess_table WHERE sess_id = '"+sess+"'", function(err,row){
			if(row.length>0){			
				responseText = 'Logged in!!';
			}else{
				responseText = 'Not Logged in!!';
			}
			res.end(JSON.stringify({'response':responseText}));
		});
	}
	catch(exception){
		console.log("Error retrieving session",exception);
		res.end(JSON.stringify({'response':'error'}));
	}			
}


app.post('/logged_in_stat', fun);
app.get('/logged_in_stat',fun);


app.post('/not_logged_in',function(req,res){
  	res.set('Content-Type', 'application/json');
	var responseText = 'Not Logged in!!';
	response = JSON.stringify({'response':responseText});
	console.log('response sent ::'+response);
	res.send(response);
});

app.listen(3000,function(){
	console.log("server running at http://127.0.0.1:3000");
});
