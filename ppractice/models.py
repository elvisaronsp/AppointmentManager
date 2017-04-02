from __future__ import unicode_literals
from django.db import models

class Doctor(models.Model):
	
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female')
		)
	docs = models.Manager()
	name = models.CharField(max_length = 200)
	age = models.IntegerField()
	gender = models.CharField(max_length = 1,choices = GENDER_CHOICES)
	clinic_address = models.TextField()
	specialisation = models.TextField()

class Patient(models.Model):
	
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female')
		)
	pats = models.Manager()
	name = models.CharField(max_length = 200)
	age = models.IntegerField()
	gender = models.CharField(max_length = 1,choices = GENDER_CHOICES)
	problem_description = models.TextField()

class Appointment(models.Model):

	date = models.DateTimeField(null=True)
	doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
	apps = models.Manager()
	patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
	status = models.BooleanField()
	cancelled_by = models.CharField(max_length=20)