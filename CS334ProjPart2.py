#This Project better utilizes data of patients to test whether they are to be
#diagnosed with heartDisease.
#Numpy used for mathematical operations
import numpy as np
#Pandas for data tabulation
import pandas as pd
#used for file reading
import csv
#pgmpy used for probablistic models
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

heartdisease = pd.read_csv('healthData.csv', encoding='utf-8')
heartdisease = heartdisease.replace('?',np.nan)

print('Sample instances from the dataset are given below')
print(heartdisease.head())

print('\n Attributes and datatypes')
print(heartdisease.dtypes)

#age is the numerical value for age of patient
#sex is denoted by either a 0 or 1. In this instance 1 would be male and 0 female
#cp is the type of chest pain that a patient is experiencing.
    #1,2,3,4 = typical, atypical, non-anginal, asymptomatic
#trestbps: resting blood pressure
#chol = cholesterol
#fbs = blood surgae greater than 120(denoted by boolean logic 1/0)
#restecg = cardiographic info. 0 = normal, 1 = abnormality
#thalach = max heart rate
#exang = excercise induced angina(1/0)
#oldpeak = exercise relative to rest
#slope = 1,2,3 = upsloping, flat, downsloping
#thal 3 is normal, 6 is fixed, 7 is reversable
#heartdisease is on a scale form 0 to 4. This indicates possible heart disease
model = BayesianNetwork([('age','heartdisease'),('sex','heartdisease'),('exang','heartdisease'),('cp','heartdisease'),('heartdisease','restecg'),('heartdisease','chol')])
print('\nLearning CPD using Maximum likelihood estimators')
model.fit(heartdisease, estimator=MaximumLikelihoodEstimator)

print('\n Inferencing with Bayesian Network:')
Heartdiseasetest_infer = VariableElimination(model)

print('\n 1. Probability of HeartDisease given evidence= restecg')
q1=Heartdiseasetest_infer.query(variables=['heartdisease'],evidence={'restecg':1})
print(q1)

print('\n 2. Probability of Heartdisease given evidence= cp ')
q2=Heartdiseasetest_infer.query(variables=['heartdisease'],evidence={'cp':2})
print(q2)