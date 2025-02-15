import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import importlib.util

from tensorflow.python.ops.gen_batch_ops import batch

app= Flask(__name__)
# file_path = os.path.join(os.getcwd(), './Bangalore/After_EDA.csv')
# Get the current working directory
# current_dir = os.path.dirname(__file__)
# print(current_dir)
# print(np.__version__)
# print(pd.__version__)


data=pd.read_csv("c:/Users/dines/Downloads/Bangalore_new/Bangalore/After_EDA.csv")
# pipe = pickle.load(open("c:/Users/harsh/Downloads/Big_D/Housing_Price/Housing_Price_Prediction/Bangalore/RidgeRegression.pkl",'rb'))
# Load the pickle file
with open("c:/Users/dines/Downloads/Bangalore_new/Bangalore/RidgeRegression.pkl", 'rb') as f:
    pipe = pickle.load(f, fix_imports=True, encoding="latin1")


@app.route('/')
def index():

    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')
    balconies = request.form.get('balconies')

    bhk = float(bhk) if bhk else None
    bath = float(bath) if bath else None
    sqft = float(sqft) if sqft else None
    

    print(location, bhk, bath, sqft)
    input = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location', 'total_sqft', 'bath', 'BHK'])
    prediction = pipe.predict(input)[0] * 1e5


    return str(np.round(prediction,2))

if __name__== "__main__":
    app.run(debug=True, port=5001)