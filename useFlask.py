import flask
import json
from flask import request, jsonify
import pandas as pd


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

if __name__ == '__main__': app.run(debug=True)
# app.run()
