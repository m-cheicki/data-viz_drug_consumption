from flask import Flask, request
import requests
import numpy as np
import pickle as p
import json

app = Flask(__name__)
model = p.load(open('models/grid_SVM_prediction.pickle', 'rb'))

person = [-0.07854, 0.48246, -1.43719, 0.96082, -0.31685,
          3.27393, -2.11437, -0.84732, -1.07533, -2.30408, 0.52975, -1.18084]


@app.route('/', methods=['GET'])
def test():
    return "test"


@app.route('/api/', methods=['GET'])
def predict():
    json = {'person': person}
    to_predict = np.array(list(json.values())).astype(float)
    return to_predict


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='5000')
