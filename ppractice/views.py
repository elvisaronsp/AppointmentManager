from django.shortcuts import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ppractice.models import *

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

@csrf_exempt
def loguserin(request):
	
	email = request['email']
	password = request['password']
	user = authenticate(email=email,password=password)
	if user is not None:
		login(request,user)
		redirect('/appointments')
	else:
		return HttpResponse("Invalid Credentials. Please try again")

@csrf_exempt
def loguserout(request):
	Doctor.docs.all().delete()
	return HttpResponse("Deleted")
	# logout(request)

@csrf_exempt
def update_appointments(request):

	p_id = request.POST.get('pid')
	d_id = request.POST.get('did')
	patient = Patient.pats.get(id=p_id)
	doctor = Doctor.docs.get(id=d_id)
	date = request.POST.get('date')
	appt = Appointment.apps.get(doctor=doctor,patient=patient)
	
	appt.update(date=date,status=True)

@csrf_exempt
def appointments(request):

	p_id = request.POST.get('pid')
	d_id = request.POST.get('did')
	patient = Patient.pats.get(id=p_id)
	doctor = Doctor.docs.get(id=d_id)
	
	if request.POST.get('requestType') == 'N':	
		new_app = Appointment(doctor=doctor,patient=patient,status=False)
		new_app.save()
	else:
		if request.POST.get('userType') == 'D':
			result = Appointment.apps.get(doctor=doctor).values()
		else:
			result = Appointment.apps.get(patient=patient).values()
	
	data = []
	for res in result:
		item = {
			'date' : res['date'],
			'doctor' : res['doctor'],
			'patient' : res['patient'],
			'status' : res['status'],
			'cancelled_by' : res['cancelled_by']
		}
		data.append(item)
	
	response['result'] = 'success'
	respone['data'] = data
	return JsonResponse(response)

@csrf_exempt
def cancel_appointment(request):
	p_id = request.POST.get('pid')
	d_id = request.POST.get('did')
	patient = Patient.pats.get(id=p_id)
	doctor = Doctor.docs.get(id=d_id)
	date = request.POST.get('date')
	appt = Appointment.apps.get(patient=patient,doctor=doctor,date=date)
	if request.POST.get('userType') == 'D':
		appt.update(cancelled_by = 'Doctor')
	else:
		appt.update(cancelled_by = 'Patient')
	appt.update(status=False)
	
@csrf_exempt
def doctor_details(request):

	doctors = Doctor.docs.all().values()
	drs = []
	for dr in doctors:
		item = {
			'name' : dr['name'],
			'age' : dr['age'],
			'specialisation' : dr['specialisation'],
			'gender' : dr['gender'],
			'clinic_address' : dr['clinic_address']
		}
		drs.append(item)

	response = {}
	response['result'] = 'success'
	response['data'] = drs
	return JsonResponse(response)

@csrf_exempt
def new_user(request):
	
	username = request['email']
	password = request['password']
	user = User(username=username,password=password)
	name = request.POST.get('name')
	age = int(request.POST.get('age'))
	gender = request.POST.get('gender')
	user.save()

	if request.POST.get('isDoctor'):		
		specialisation = request.POST.get('specialisation')
		clinic_address = request.POST.get('clinic_address')
		doc = Doctor(user=user,name=name,age=age,gender=gender,specialisation=specialisation,clinic_address=clinic_address)
		doc.save()
	else:
		problem_description = request.POST.get('problem_description')
		pat = Patient(user=user,name=name,age=age,gender=gender,problem_description=problem_description)
		pat.save()
	res = {}
	res['result'] = 'success'
	return JsonResponse(res)
