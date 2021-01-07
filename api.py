from tensorflow.keras.models import load_model

model = load_model('model.h5','rb')
load_model =  model.load_weights('model.h5')
