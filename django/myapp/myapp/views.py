from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")

def aboutUS(request):
    return HttpResponse("Welcome !!")
