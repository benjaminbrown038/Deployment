from tensorflow.keras.models import load_model

    
model = load_model('model.h5')
load_model =  model.load_weights('model.h5')

results = load_model.predict_classes()
