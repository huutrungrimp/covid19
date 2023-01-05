from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
import pandas as pd
import json
from pathlib import Path
import os
import datetime
from urllib.error import HTTPError
import numpy

def getOnEpi():    
    newData = pd.read_csv("https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv")
    newData= newData.fillna(0)
    col = newData.columns.str.lower()
    col = col.str.replace(' ', '_')
    col = col.str.replace('-', '')
    col = col.str.replace(',', '')
    col = col.str.replace('.', '', regex=True)
    newData.columns = col
    return newData          


def getDemographyData():
    conf_phu = pd.read_csv("https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv", usecols = ['Case_Reported_Date', 'Age_Group', 'Client_Gender'], low_memory = True)
    conf_phu['count']=1

    age = conf_phu[['Case_Reported_Date', 'Age_Group']]
    age=conf_phu.groupby(['Case_Reported_Date', 'Age_Group']).count().reset_index()
    age=age.pivot(index='Case_Reported_Date', columns='Age_Group', values='count')
    
    result = age.to_json(orient="table")
    parsed = json.loads(result)
    age_json = parsed['data']
    age_json

    gender = conf_phu[['Case_Reported_Date', 'Client_Gender', 'count']]
    gender=gender.groupby(['Case_Reported_Date', 'Client_Gender']).count().reset_index()
    gender=gender.pivot(index='Case_Reported_Date', columns='Client_Gender', values='count')
    result = gender.to_json(orient="table")
    parsed = json.loads(result)
    gender_json = parsed['data']
    gender_json

    demography = {
        'age': age_json,
        'gender':gender_json
    }
    return demography