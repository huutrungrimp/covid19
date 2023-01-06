from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
import pandas as pd
import json
from pathlib import Path
import os
import datetime
import pandas as pd
from urllib.error import HTTPError
from .getData import getOnEpi, getDemographyData
# import numpy
from memory_profiler import profile


@profile
def epiGraph_ON(request):
    epi_phu = getOnEpi()
    active = epi_phu.groupby(['reported_date']).sum()
    active_json = active.to_json(orient="table")
    ontario = json.loads(active_json)

    return JsonResponse(ontario['data'], safe=False)

@profile
def epiDemography_ON(request):
    demographyData = getDemographyData()
    return JsonResponse(demographyData, safe=False)

if __name__ == '__main__':
    epiDemography_ON