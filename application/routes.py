from application import app, db
from flask import render_template, request, Response, json

jsondata = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, 
	{"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"},
	 {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, 
	 {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, 
	 {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]
@app.route('/')

@app.route('/index')
def index():
	return render_template("index.html", login=False)

@app.route('/login')
def login():
	return render_template("login.html", login=True)

@app.route('/courses/')
@app.route('/courses/<term>')
def courses(term="Spring 2023"):
	
	return render_template("courses.html", courseData = jsondata, courses = True, term=term)

@app.route('/register')
def register():
	return render_template("register.html", register=True)

@app.route('/enrollment', methods=["GET","POST"])
def enrollment():
	id = request.form.get('courseID')
	title = request.form['title']
	term = request.form.get('term')
	return render_template("enrollment.html", enrollment=True, courseData={"id":id,"title":title,"term":term})

@app.route('/api/')
@app.route('/api/<idx>')
def api(idx=None):
	if (idx==None):
		jdata = jsondata
	else:
		jdata = jsondata[int(idx)]

	return Response(json.dumps(jdata), mimetype="application/json")

class User(db.Document):
	user_id = db.IntField( unique = True )
	first_name = db.StringField( max_length=50 )
	last_name = db.StringField( max_length=50 )
	email = db.StringField(max_length =30 )
	password = db.StringField( max_length= 30)

@app.route("/user")
def user():
	# User(user_id=1, first_name="Jens", last_name="Shumway", email="christian@uta.com", password="abcdef").save()
	# User(user_id=2, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
	users = User.objects.all()
	return render_template("user.html", users=users)


