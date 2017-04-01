from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
	pass

@csrf_exempt
def appointments(request,date):
	pass

def new_appointment(request,date):
	pass

def cancel_appointment(request):
	pass

def doctor_details(request,id):
	pass