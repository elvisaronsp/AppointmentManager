from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def login(request):
	pass

def appointments(request):

	p_id = request.POST.get('pid')
	d_id = request.POST.get('did')
	patient = Patient.pats.get(id=p_id)
	doctor = Doctor.docs.get(id=d_id)
	result = []
	
	if request.POST.get('requestType') == 'N':	
		new_app = Appointment(doctor=doctor,patient=patient,status=False)
		new_app.save()
	else:
		if request.POST.get('userType') == 'D':
			result = Appointment.apps.get(doctor=doctor).values()
		else:
			result = Appointment.apps.get(patient=patient).values()
	
	response['result'] = 'success'
	respone['data'] = result
	return JsonResponse(response)

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
	

def doctor_details(request,id):

	doctors = Doctor.docs.all().values()
	response['result'] = 'success'
	response['data'] = doctors
	return JsonResponse(response)

def new_user(request):
	
	if request.POST.get('userType') == 'D':
		name = request.POST.get('name')
		age = int(request.POST.get('age'))
		gender = request.POST.get('gender')
		specialisation = request.POST.get('specialisation')
		clinic_address = request.POST.get('clinic_address')
		doc = Doctor(name=name,age=age,gender=gender,specialisation=specialisation,clinic_address=clinic_address)
		doc.save()
	else:
		name = request.POST.get('name')
		age = int(request.POST.get('age'))
		gender = request.POST.get('gender')
		problem_description = request.POST.get('problem_description')
		pat = Patient(name=name,age=age,gender=gender,problem_description=problem_description)
		pat.save()