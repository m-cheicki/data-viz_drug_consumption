import pickle
import numpy as np

model = pickle.load(open('models/grid_SVM_prediction.pickle', 'rb'))
person = [-0.07854, 0.48246, -1.43719, 0.96082, -0.31685, 3.27393, -2.11437, -0.84732, -1.07533, -2.30408, 0.52975, -1.18084]
json = {'person': person}
to_predict = np.array(list(json.values())).astype(float)
print(to_predict)
print(model.predict(to_predict))  # CL6


