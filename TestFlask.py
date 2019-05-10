from flask import Flask
app = Flask(__name__)
@app.route('/')
def testflask():
    return "This is Flask"
