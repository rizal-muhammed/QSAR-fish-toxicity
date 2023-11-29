from flask import Flask,render_template,json,jsonify,request
import pickle
import numpy as np
from pathlib import Path
import os


app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def training():
    os.system("python3 main.py")
    return "Training Successful"


@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        CIC0=float(request.form['CIC0'])
        SM1_Dz=float(request.form['SM1_Dz'])
        GATS1i=float(request.form['GATS1i'])
        NdsCH=float(request.form['NdsCH'])
        NdssC=float(request.form['NdssC'])
        MLOGP=float(request.form['MLOGP'])

        # load the pickle file
        filepath = Path("artifacts/model_training/best_model/best_model.pkl")
        with open(filepath, "rb") as file:
            best_model = pickle.load(file)
        
        input = np.array([[CIC0, SM1_Dz, GATS1i, NdsCH, NdssC, MLOGP]], dtype=float)
        predicted_LC50 = best_model.predict(input)

        #get the result template
        return render_template('result.html',prediction=predicted_LC50)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)