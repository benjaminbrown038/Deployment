import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)
#model = pickle.load(open('model.h5', 'rb'))
deploy_model = load_model('./model.h5',compile=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():
    cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    #src is the source, original or input image in the form of numpy array
    #dsize is the desired size of the output image, given as tuple
    #fx is the scaling factor along X-axis or Horizontal axis
    def check_input_size(i)

    data = request.get_json(force=True)
    prediction = deploy_model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
