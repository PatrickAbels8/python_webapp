from flask import Flask, request, render_template, escape, url_for, redirect
import os

# MAIN FUNCTION
def getData(json):
	return 'Search for %s gives: tba' % json

# create Flask with reference to style sheet
app = Flask(__name__, static_url_path='/static')
DEFAULT_PORT = 2000

# infos about HTTP: https://www.tutorialspoint.com/flask/flask_http_methods.htm
@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	elif request.method == 'POST':
		return getData(request.form['json'])

@app.route('/doc')
@app.route('/docu')
@app.route('/documentation')
def documentation():
 	return render_template('doc.html')

@app.route('/images')
@app.route('/imgs')
def images():
	return render_template('images.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/references')
@app.route('/ref')
@app.route('/refs')
def referneces():
	return render_template('references.html')
	
# progress page for all the redirects
# use with: return redirect(url_for('inprogress'))
@app.route('/inprogress')
def inprogress():
	return 'not finished yet... :('

if __name__ == '__main__':
	# url_for('static', filename='style.css')
	port = os.environ.get('PORT', DEFAULT_PORT)
	# host='0.0.0.0' for global access
	app.run(port=port)