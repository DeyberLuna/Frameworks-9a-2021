from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def autoview(request):

    return HttpResponse('Esta es una vista de auto')