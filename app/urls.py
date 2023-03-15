from app.views import *
from django.urls import path
app_name='app'
urlpatterns=[
    path('pinky/',pinky,name='pinky'),
]

