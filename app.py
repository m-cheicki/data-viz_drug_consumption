from flask import Flask, request, jsonify, render_template
import requests
import numpy as np
import pickle as p
import json

app = Flask(__name__, template_folder='views')


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/alcohol/', methods=["POST"])
def alcohol():
    model = p.load(open('models/ALCOHOL_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/amphet/', methods=["POST"])
def amphet():
    model = p.load(open('models/AMPHET_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/amyl/', methods=["POST"])
def amyl():
    model = p.load(open('models/AMYL_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/benzos/', methods=["POST"])
def benzos():
    model = p.load(open('models/BENZOS_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/caffeine/', methods=["POST"])
def caffeine():
    model = p.load(open('models/CAFFEINE_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/cannabis/', methods=["POST"])
def cannabis():
    model = p.load(open('models/CANNABIS_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/chocolate/', methods=["POST"])
def chocolate():
    model = p.load(
        open('models/CHOCOLATE_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/coke/', methods=["POST"])
def coke():
    model = p.load(open('models/COKE_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/crack/', methods=["POST"])
def crack():
    model = p.load(open('models/CRACK_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/ectasy/', methods=["POST"])
def ectasy():
    model = p.load(open('models/ECSTASY_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/heroin/', methods=["POST"])
def heroin():
    model = p.load(open('models/HEROIN_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/ketamine/', methods=["POST"])
def ketamine():
    model = p.load(open('models/KETAMINE_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/legal-highs/', methods=["POST"])
def lh():
    model = p.load(
        open('models/LEGAL_HIGHS_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/lsd/', methods=["POST"])
def lsd():
    model = p.load(open('models/LSD_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/magic-mushrooms/', methods=["POST"])
def mm():
    model = p.load(
        open('models/MAGIC_MUSHROOMS_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/meth/', methods=["POST"])
def meth():
    model = p.load(open('models/METH_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/nicotine/', methods=["POST"])
def nicotine():
    model = p.load(open('models/NICOTINE_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/semer/', methods=["POST"])
def semer():
    model = p.load(open('models/SEMER_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


@app.route('/vsa/', methods=["POST"])
def vsa():
    model = p.load(open('models/VSA_CONSUMPTION_prediction.pickle', 'rb'))
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='5000')
