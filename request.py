import requests
import numpy as np
import json

url = 'http://localhost:5000/api/'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

person = [-0.07854, 0.48246, -1.43719, 0.96082, -0.31685,
          3.27393, -2.11437, -0.84732, -1.07533, -2.30408, 0.52975, -1.18084]
j_data = json.dumps({'person': person})
# to_predict = np.array(list(json.values())).astype(float)

r = requests.post(url, data=j_data, headers=headers)
print(r.url)
print(r.text)
