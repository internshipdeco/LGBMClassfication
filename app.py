# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:40:44 2021

@author: SHRIKRISHNA
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import json


app = Flask(__name__,template_folder='templates')
model = pickle.load(open('mahinLog.pkl', 'rb'))

#function to read binary excel file and return dataframe

@app.route('/')
def home():
    df = pd.read_csv("submission.csv")
    with open('result.json', 'r') as myfile:
        data = myfile.read()
    jsondata = json.loads(data)
  
    return render_template("index.html", result = jsondata, tables=[df.head(50).to_html(classes='data',  index= False)], titles=df.columns.values)
    #return 'Hello World'
 

if __name__ == "__main__":
    app.run(debug=True)

