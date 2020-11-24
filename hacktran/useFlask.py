import flask
import json
from flask import request, jsonify
import pandas as pd

df = pd.read_csv ('acidenteTransito.csv', sep=",") 

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>API para acidentes no transito</h1>'''

@app.route('/all', methods=['GET'])
def api_all():
    result = df[:50000].to_json(orient="index")
    parsed = json.loads(result)
    data = json.dumps(parsed, indent=4)
    return jsonify(data)

@app.route('/lat', methods=['GET'])
def api_lat():
    result = df["lat"].to_json(orient="index")
    parsed = json.loads(result)
    data = json.dumps(parsed, indent=4)
    return jsonify(data)

@app.route('/long', methods=['GET'])
def api_long():
    result = df["long"].to_json(orient="index")
    parsed = json.loads(result)
    data = json.dumps(parsed, indent=4)
    return jsonify(data)

@app.route('/class', methods=['GET'])
def api_class():
    result = df["class"].to_json(orient="index")
    parsed = json.loads(result)
    data = json.dumps(parsed, indent=4)
    return jsonify(data)

@app.route('/mortos', methods=['GET'])
def api_mortos():
    result = df["mortos"].to_json(orient="index")
    parsed = json.loads(result)
    data = json.dumps(parsed, indent=4)
    return jsonify(data)

@app.route('/feridos', methods=['GET'])
def api_feridos():
    result = df["feridos"].to_json(orient="index")
    parsed = json.loads(result)
    data = json.dumps(parsed, indent=4)
    return jsonify(data)

@app.route('/br', methods=['GET'])
def api_br():
    result = df["br"].to_json(orient="index")
    parsed = json.loads(result)
    data = json.dumps(parsed, indent=4)
    return jsonify(data)

@app.route('/km', methods=['GET'])
def api_km():
    result = df["km"].to_json(orient="index")
    parsed = json.loads(result)
    data = json.dumps(parsed, indent=4)
    return jsonify(data)

@app.route('/fatais', methods=['GET'])
def api_fatais():
    fatais = []
    for i in range(len(df["class"])):
        if df["class"][i] == 3:
            fatais.append({"lat": df["lat"][i], "long": df["long"][i]})
    return jsonify(fatais)

@app.route('/acidentesLeves', methods=['GET'])
def api_acidentesLeves():
    acidentesLeves = []
    for i in range(len(df["class"])):
        if df["class"][i] == 1:
            acidentesLeves.append({"lat": df["lat"][i], "long": df["long"][i]})
    return jsonify(acidentesLeves)

@app.route('/acidentesPesados', methods=['GET'])
def api_acidentesPesados():
    acidentesPesados = []
    for i in range(len(df["class"])):
        if df["class"][i] == 2:
            acidentesPesados.append({"lat": df["lat"][i], "long": df["long"][i]})
    return jsonify(acidentesPesados)

if __name__ == '__main__': app.run(debug=True)
# app.run()
