from flask import Flask, flash, render_template, request, redirect, url_for
from models.models import *

app = Flask(__name__)
app.secret_key = 'some_secret'



@app.before_request
def before_request():
	# create db if needed and connect
	initialize_db()



@app.teardown_request
def teardown_request(exception):
	# close the db connection
	db.close()



@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404



@app.route('/')
def home():
	# render the home page with the saved posts
	return render_template('home.html', posts=Post.select().order_by(Post.date.desc()))



@app.route('/new_post/')
def new_post():
	return render_template('new_post.html')



@app.route('/create/', methods=['POST'])
def create_post():
	# create the new post
	Post.create(
		title=request.form['title'],
		text=request.form['text']
	)

	# return the user to the homepage
	return redirect(url_for('home'))



@app.route('/register/', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		# check if the user exists
		query = Users.select().where(Users.username == username)
		if query.exists():
			# user exists. send error to register.html
			flash('User already exists!')
			return redirect(url_for('register'))
		else:
			# create the user
			Users.create(
				username=username,
				password=password
			)
			return redirect(url_for('home'))
			
	return render_template('register.html')
	


if __name__ == "__main__":
    app.run(debug=True)
