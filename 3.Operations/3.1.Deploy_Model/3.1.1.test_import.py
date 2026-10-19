import pickle
import numpy as np

filename = 'my_saved_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
predict = np.array([4]).reshape(1, -1)
result = loaded_model.predict(predict)
print(result[0])
