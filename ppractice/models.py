from __future__ import unicode_literals
from django.db import models

class Doctor(model.Models):
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female')
		)
	id = models.AutoField(primary_key = True)
	name = models.CharField(maxlength = 200)
	age = models.IntegerField()
	gender = models.CharField(maxlength = 1,choices = GENDER_CHOICES)
	clinic_address = models.TextField()

class Appointment(models.Models):
	
	date = models.DateTimeField()
	doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
