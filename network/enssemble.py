from tensorflow import keras
# import keras
import numpy as np
from preprocessing.utils import accuracy_m
from network.nn import DNN_A, DNN_B, CNN_A, CNN_B, CNN_C 

def semble_transfer(opt, X_test, y_test):
  y_pred = np.zeros(shape=y_test.shape)
  l = 0
  
  for name in opt.model_names:
    all_path = opt.model_dir + name 
    if name == 'CNN_A':
      model = CNN_A(opt)
    elif name == 'CNN_C':
      model = CNN_C(opt)
    
    if name == 'CNN_A' or name == 'CNN_C':
      model.load_weights(all_path)
      curr_y_pred = model.predict(X_test)
      keras.backend.clear_session()
      np.save(opt.model_dir + name + '.npy', curr_y_pred)
    
      y_pred += curr_y_pred
      l += 1
      keras.backend.clear_session()
    
  y_pred = y_pred / l
  print('Test accuracy: ', accuracy_m(y_test, y_pred))
    
