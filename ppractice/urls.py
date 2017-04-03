from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^loguserin/$',views.login,name='loguserin'),
	url(r'^appointments/$',views.appointments,name='appointments'),
	url(r'^cancel_appointment/$',views.cancel_appointment,name='cancel_appointment'),
	url(r'^doctor_details/$',views.doctor_details,name='doctor_details'),
	url(r'^new_user/$',views.new_user,name='new_user'),
	url(r'^update_appt/$',views.update_appointments,name='update_appts'),
	url(r'^loguserout/$',views.loguserout,name='loguserout')
]