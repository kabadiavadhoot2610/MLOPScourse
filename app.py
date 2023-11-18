from flask import Flask, request, jsonify
import os
from joblib import load

app = Flask(__name__)

@app.route('/hello/<name>')
def index(name):
    return "Hello, "+name+"!"

@app.route('/predict',methods=['POST'])
def predict_image():
    try:
        js = request.get_json()
        
        img = js['image']
        
        directory = os.path.dirname(__file__)
        file = os.path.join(directory,'../models/svmgamma:0.001_C:1.joblib')
        
        model = load(file)
        predict= model.predict(img)
        
        return jsonify(prediction=predict.tolist())
    except Exception as e:
        return jsonify(error=str(e))
        

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
