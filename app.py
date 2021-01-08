from flask import Flask, request, jsonify
import requests
import numpy as np
import pickle as p
import json

app = Flask(__name__)

@app.route('/api/', methods=["POST"])
def post_predict():
    return jsonify(np.array2string(model.predict([request.get_json()['person']])))

if __name__ == '__main__':
    model = p.load(open('models/svm_prediction.pickle', 'rb'))
    app.run(debug=True, host='localhost', port='5000')
