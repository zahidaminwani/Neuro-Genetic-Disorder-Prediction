from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import random
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

import requests
from datetime import datetime, timezone, timedelta


def getPredictions(age, gender, ethnicity, education_level, bmi, smoking, alcohol_consumption, physical_activity, 
                   family_history_alzheimers, cardiovascular_disease, diabetes, head_injury, hypertension,
                   diastolic_bp, cholesterol_hdl, behavioral_problems, adl, confusion, forgetfulness):
    model = pickle.load(open('Models/Alzi_DT.pkl', 'rb'))
    # Updated feature set
    new_data = {
        'Age': age,
        'Gender': gender,
        'Ethnicity': ethnicity,
        'EducationLevel': education_level,
        'BMI': bmi,
        'Smoking': smoking,
        'AlcoholConsumption': alcohol_consumption,
        'PhysicalActivity': physical_activity,
        'FamilyHistoryAlzheimers': family_history_alzheimers,
        'CardiovascularDisease': cardiovascular_disease,
        'Diabetes': diabetes,
        'HeadInjury': head_injury,
        'Hypertension': hypertension,
        'DiastolicBP': diastolic_bp,
        'CholesterolHDL': cholesterol_hdl,
        'BehavioralProblems': behavioral_problems,
        'ADL': adl,
        'Confusion': confusion,
        'Forgetfulness': forgetfulness
    }
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)
    return prediction[0]




def result(request):
    # Retrieving data from the request for the updated features
    age = int(request.GET['Age'])
    gender = str(request.GET['Gender'])
    ethnicity = str(request.GET['Ethnicity'])
    education_level = str(request.GET['EducationLevel'])
    bmi = float(request.GET['BMI'])
    smoking = str(request.GET['Smoking'])
    alcohol_consumption = str(request.GET['AlcoholConsumption'])
    physical_activity = str(request.GET['PhysicalActivity'])
    family_history_alzheimers = str(request.GET['FamilyHistoryAlzheimers'])
    cardiovascular_disease = str(request.GET['CardiovascularDisease'])
    diabetes = str(request.GET['Diabetes'])
    head_injury = str(request.GET['HeadInjury'])
    hypertension = str(request.GET['Hypertension'])
    diastolic_bp = float(request.GET['DiastolicBP'])
    cholesterol_hdl = float(request.GET['CholesterolHDL'])
    behavioral_problems = str(request.GET['BehavioralProblems'])
    adl = str(request.GET['ADL'])
    confusion = str(request.GET['Confusion'])
    forgetfulness = str(request.GET['Forgetfulness'])
    
    # Calling getPredictions with the updated feature set
    result = getPredictions(age, gender, ethnicity, education_level, bmi, smoking, alcohol_consumption, physical_activity, 
                            family_history_alzheimers, cardiovascular_disease, diabetes, head_injury, hypertension,
                            diastolic_bp, cholesterol_hdl, behavioral_problems, adl, confusion, forgetfulness)
    
    if result==1:
        result="Alzheimer Disease"
    else:
        result="Healthy"
    # Returning the result to the template
    return render(request, 'result.html', {'result': result})


def getPredictions2(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    model = pickle.load(open('Models/Epl_DT.pkl', 'rb'))
    new_data = {
        'X1': x1,
        'X2': x2,
        'X3': x3,
        'X4': x4,
        'X5': x5,
        'X6': x6,
        'X7': x7,
        'X8': x8,
        'X9': x9,
        'X10': x10
    }
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)
    return prediction[0]

def result2(request):
    # Retrieving data from the request for the updated features
    x1 = float(request.GET['X1'])
    x2 = float(request.GET['X2'])
    x3 = float(request.GET['X3'])
    x4 = float(request.GET['X4'])
    x5 = float(request.GET['X5'])
    x6 = float(request.GET['X6'])
    x7 = float(request.GET['X7'])
    x8 = float(request.GET['X8'])
    x9 = float(request.GET['X9'])
    x10 = float(request.GET['X10'])
    
    # Calling getPredictions with the new feature set
    result = getPredictions2(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)
    if result==1:
        result=" Recording of seizure activity"
    elif result==2:
        result="They recorder the EEG from the area where the tumor was located"
    elif result==3:
        result="Yes they identify where the region of the tumor was in the brain and recording the EEG activity from the healthy brain area"
    elif result==4:
        result="eyes closed, means when they were recording the EEG signal the patient had their eyes closed"
    else:
        result="eyes open, means when they were recording the EEG signal of the brain the patient had their eyes open"
    # Returning the result to the template
    return render(request, 'result2.html', {'result': result})


def getPredictions3(age, gender, cag_repeats, motor_score, cognitive_score, behavioral_score, family_history):
    model = pickle.load(open('Models/H_KNN.pkl', 'rb'))
    # Updated feature set
    new_data = {
        'Age': age,
        'Gender': gender,
        'CAG_Repeats': cag_repeats,
        'Motor_Score': motor_score,
        'Cognitive_Score': cognitive_score,
        'Behavioral_Score': behavioral_score,
        'Family_History': family_history
    }
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)
    return prediction[0]

def result3(request):
    # Retrieving data from the request for the updated features
    age = int(request.GET['Age'])
    gender = str(request.GET['Gender'])
    cag_repeats = float(request.GET['CAG_Repeats'])
    motor_score = float(request.GET['Motor_Score'])
    cognitive_score = float(request.GET['Cognitive_Score'])
    behavioral_score = float(request.GET['Behavioral_Score'])
    family_history = int(request.GET['Family_History'])
    
    # Calling getPredictions with the new feature set
    result = getPredictions3(age, gender, cag_repeats, motor_score, cognitive_score, behavioral_score, family_history)
    # Returning the result to the template
    return render(request, 'result3.html', {'result': result})

def getPredictions4(fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, jitter_ddp, shimmer, shimmer_db, shimmer_apq3, shimmer_apq5, apq, shimmer_dd, nhr, hnr):
    model = pickle.load(open('Models/parkinson_KNN.pkl', 'rb'))
    # Updated feature set
    new_data = {
        'MDVP:Fo(Hz)': fo,
        'MDVP:Fhi(Hz)': fhi,
        'MDVP:Flo(Hz)': flo,
        'MDVP:Jitter(%)': jitter_percent,
        'MDVP:Jitter(Abs)': jitter_abs,
        'MDVP:RAP': rap,
        'MDVP:PPQ': ppq,
        'Jitter:DDP': jitter_ddp,
        'MDVP:Shimmer': shimmer,
        'MDVP:Shimmer(dB)': shimmer_db,
        'Shimmer:APQ3': shimmer_apq3,
        'Shimmer:APQ5': shimmer_apq5,
        'MDVP:APQ': apq,
        'Shimmer:DDA': shimmer_dd,
        'NHR': nhr,
        'HNR': hnr
    }
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)
    return prediction[0]
def result4(request):
    # Retrieving data from the request for the updated features
    fo = float(request.GET['a'])
    fhi = float(request.GET['MDVP:Fhi(Hz)'])
    flo = float(request.GET['MDVP:Flo(Hz)'])
    jitter_percent = float(request.GET['MDVP:Jitter(%)'])
    jitter_abs = float(request.GET['MDVP:Jitter(Abs)'])
    rap = float(request.GET['MDVP:RAP'])
    ppq = float(request.GET['MDVP:PPQ'])
    jitter_ddp = float(request.GET['Jitter:DDP'])
    shimmer = float(request.GET['MDVP:Shimmer'])
    shimmer_db = float(request.GET['MDVP:Shimmer(dB)'])
    shimmer_apq3 = float(request.GET['Shimmer:APQ3'])
    shimmer_apq5 = float(request.GET['Shimmer:APQ5'])
    apq = float(request.GET['MDVP:APQ'])
    shimmer_dd = float(request.GET['Shimmer:DDA'])
    nhr = float(request.GET['NHR'])
    hnr = float(request.GET['HNR'])
    
    # Calling getPredictions with the new feature set
    result = getPredictions4(fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, jitter_ddp, shimmer, shimmer_db, shimmer_apq3, shimmer_apq5, apq, shimmer_dd, nhr, hnr)
    
    if result==1:
        result="Parkinson Disease"
    else:
        result="Healthy"
    return render(request, 'result4.html', {'result': result})



def HomePage(request):
   return render(request, 'home.html')

def index(request):
   return render(request, 'index.html')

def index2(request):
   return render(request, 'index2.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')