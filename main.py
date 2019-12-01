# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests

# Create the application
app = flask.Flask(__name__)

API_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&locationbias=ipbias&fields=formatted_address,name,rating"

@app.route('/')
def hello():
    return "Hello World!"

# path parameters
@app.route('/<name>')
def personal_hello(name):
	return "Hello "+name

# serving hello.html
@app.route('/fancy/<name>')
def some_page(name):
	return flask.render_template('hello.html', name=name)

# serving find.html
@app.route('/find', methods=['GET'])
def find():
	return flask.render_template('find.html')

# process query
@app.route('/process_query', methods=['POST'])
def process_query():
	data = flask.request.form
	location = data['some_location']
	print(location)

	requestString = formRequest(location)
	responses = makeGET(requestString)['candidates']
	return flask.render_template('find.html', responses=responses)

@app.route('/button', methods=['GET','POST'])
def button():
	return flask.render_template('button.html')

def formRequest(input):
	return API_URL + "&key=" + readKey() + "&input=" + input

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

def makeGET(input):
	# TODO
	response = requests.get(input).json()
	if response:
		return response
	else:
		return "Error: No response entered"

def readKey():
	f = open("secrets.txt", "r")
	contents = f.read()
	return contents.strip()

if __name__ == '__main__':
    app.run(debug=True)
