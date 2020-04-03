#import
#import <filename>
#from filename import <....>
from flask import Flask 

#calling/ instanciating
app = Flask(__name__)

#creating of endpoins/ route
#1. declaration of a route
#2. a function embede to the route
# route -outputs to web-browser
@app.route('/')
def hello_world():
    return '<h1>Welcome to web development</h1>'

@app.route('/home')
def home():
    return '<h1> Welcome to home </h1>'

@app.route('/service')
def service():
    return '<h1> Welcome to service </h1>'

@app.route('/contact_us')
def contact_us():
    return '<h1> Welcome to service </h1>'

@app.route ('/about')
def about():
    return '<h1> Welcome to about</h>'

@app.route('/name/<name>')
def my_name(name):
   #return f'My name is{name}'
   return 'My name is {}'. format (name)
    #return 'My name is ' +name

#add two number dynamically
@app.route ('/add/<n1>/<n2>')
def add(n1, n2):
    sum = int(n1)+int(n2)
    return str(sum)

#divide
@app.route ('/divide/<n1>/<n2>')
def divide(n1, n2):
    division = int(n1)/int(n2)
    return str(division)

#multiply
@app.route ('/multiply/<n1>/<n2>')
def multiply (n1,n2):
    multiple = int(n1)*int(n2)
    return str (multiple)

#output: your story (name, age, town)
@app.route ('/story/<name>/<age>/<town>')
def story (name,age,town):
    return 'My name is{}'.format(name), 'I am {} old'.format(age) + 'I come from {}'. format (town)

# Run your app
if __name__ =='__main__':
    app.run()

