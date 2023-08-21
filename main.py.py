# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:37:12 2023

@author: user
"""

from fastapi import FastAPI
from pydantic import BaseModel
import json 
import pickle

app = FastAPI()

class ModelInput(BaseModel):
    pregnancies: int
    glucose: int
    bloodpressure: int
    skinthickness: int
    insulin: int
    BMI: float
    diabetes: float
    age: int


# loading the model

diabetes = pickle.load(open('trained_mode.sav','rb'))

@app.post('/diabetes_prediction')


def diabetes_prediction(input_parameters:ModelInput):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['pregnancies']
    glu = input_dictionary['glucose']
    bp = input_dictionary['bloodpressure']
    skin = input_dictionary['skinthickness']
    insulin = input_dictionary['insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['diabetes']
    age = input_dictionary['age']

    input_list = [preg,glu,bp,skin,insulin,bmi,dpf,age]
    prediction = diabetes.predict([input_list])

    if prediction[0]==0:
        return 'the person is not diabetic'
    
    else:

        return 'the person is diabetic'
    