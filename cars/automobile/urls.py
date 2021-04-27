from django.urls import path
from . import views
from automobile.views import *

urlpatterns=[
    path('',views.autoview,name='auto')
]