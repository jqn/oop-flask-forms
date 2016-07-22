from flask import Flask # Import flask class
app = Flask(__name__) # Create an instance of flask class

@app.route('/') # Route decorator tells flask what URL shoudl be triggered
def hello_world():
    return 'Hello World!'
