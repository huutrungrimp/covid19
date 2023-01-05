from django.urls import path
from . import views


APP_NAME='ontario'

urlpatterns = [
    path('graphs', views.epiGraph_ON, name='epiGraph_ontario'), #epi: confirmed, active_cases, resolved_cases, deaths  
    path('demography', views.epiDemography_ON, name='epidemography_ON'),
    # path('maps/<str:epi>', views.epiMap_ON, name='epiMap_ontario'),
]