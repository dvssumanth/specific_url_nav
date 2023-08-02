from django.urls import path
from app.views import *
app_name='app'
urlpatterns=[
    path('dvs/',dvs,name='dvs')
]