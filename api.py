from flask import Flask, render_template, escape, url_for, redirect
import os

# create Flask with reference to style sheet
app = Flask(__name__, static_url_path='/static')
DEFAULT_PORT = 2000

# connect url / with say_hello method
@app.route('/')
def say_hello():
	return 'Hello, World!'

# use variables in url
@app.route('/user/<username>')
def show_username(username):
	return 'Welcome, User %s!' % escape(username)

# start html template
@app.route('/doc')
def open_documentation():
 	return render_template('doc.html')

# pages that aren't finished yet
@app.route('/images')
@app.route('/about')
def load_images():
	return redirect(url_for('inprogress'))

# progress page for all the redirects
@app.route('/inprogress')
def inprogress():
	return 'not finished yet... :('

if __name__ == '__main__':
	# url_for('static', filename='style.css')
	port = os.environ.get('PORT', DEFAULT_PORT)
	# host='0.0.0.0' for global access
	app.run(port=port)