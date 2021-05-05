from django.shortcuts import render
from .models import *

def home(request):
	return render(request,'index.html')

def servicios(request):
	return render(request,'services.html')

def contacto(request):
	return render(request,'contact.html')