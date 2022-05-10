from flask import Flask,jsonify,request
from scrape import validate

# Simple flask app
app = Flask(__name__)

@app.route('/scrape')
def scrape():
    data = {
        "username": request.args.get('username'),
        "validated": validate(request.args.get('username'))
    }
    return jsonify(data)
