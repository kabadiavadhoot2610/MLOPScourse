from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

def classify_digits(image_path):
    digit = int(image_path.split('_')[-1].split('.')[0])
    return digit

@app.route("/",methods=['POST'])
def compare_digits():
    image1 = request.files['image1']
    image2 = request.files['image2']
    
    digit1 = classify_digits(image1)
    digit2 = classify_digits(image2)
    
    result = digit1==digit2
    
    return jsonify({'result':result})

if __name__=='__main__':
    app.run(debug=True)