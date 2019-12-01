# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests

# Create the application
app = flask.Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template('hello.html')

# path parameters
@app.route('/<name>')
def personal_hello(name):
	return "Hello "+name

# serving hello.html
@app.route('/fancy/<name>')
def some_page(name):
	return flask.render_template('hello.html', name=name)

@app.route('/upvote')
def testbutton():
	return flask.render_template('upvote.html')

@app.route('/search')
def search():
	return flask.render_template('search.html')

@app.route('/searchfilter')
def searchfilter():
	return flask.render_template('searchfilter.html')

@app.route('/filter')
def filter():
	return flask.render_template('filter.html')

@app.route('/milestones')
def makeMilestone():
    return flask.render_template('milestones.html')

def makeGET(input):
	# TODO
	response = requests.get(input).json()
	if response:
		return response
	else:
		return "Error: No response entered"

if __name__ == '__main__':
    app.run(debug=True)
