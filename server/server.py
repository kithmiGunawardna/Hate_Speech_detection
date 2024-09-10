import util

from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route("/predict_hate_speech",methods = ['GET','POST'])
def predict_hate_speech():
    sentence = request.form["sentence"]
    response = jsonify({'prediction':util.prediction([sentence])})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ =='__main__' :
    util.load_dataset()
    util.tokanization()
    util.load_model()
    app.run()
    
