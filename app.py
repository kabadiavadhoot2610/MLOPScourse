from flask import Flask, request, jsonify
import os
from joblib import load
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods=["POST"])
def hello_world_post():    
    return {"op" : "Hello, World POST " + request.json["suffix"]}

# @app.route('/hello/<name>')
# def index(name):
#     return "Hello, "+name+"!"

def load_model(model_name):
    dirname = os.path.dirname(__file__)
    filename_svm = os.path.join(dirname, '../models/svmgamma:0.001_C:1.joblib')
    svm = load(filename_svm)
    filename_tree = os.path.join(dirname, '../models/treemax_depth:100.joblib')
    tree = load(filename_tree)
    filename_lr = os.path.join(dirname, '../models/D23CSA001_lr_newton-cg.joblib')
    lr = load(filename_lr)
    if model_name == 'svm':
        return svm
    elif model_name == 'tree':
        return tree
    elif model_name == 'lr':
        return lr
    else:
        return None

@app.route('/predict',methods=['POST'])
def predict_image():
    try:
        js = request.get_json()
        model_name = escape(model_name)
        img = [js['image']]
        model = load_model(model_name)
        predict= model.predict(img)
        
        return jsonify(prediction=predict.tolist())
    except Exception as e:
        return jsonify(error=str(e))

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
