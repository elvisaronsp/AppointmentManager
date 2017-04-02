from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^login/$',views.login,name='login'),
	url(r'^appointments/$',views.appointments,name='appointments'),
	url(r'^cancel_appointment/$',views.cancel_appointment,name='cancel_appointment'),
	url(r'^doctor_details/$',views.doctor_details,name='doctor_details'),
	url(r'^new_user/$',views.new_user,name='new_user'),
	url(r'^update_appt/$',views.update_appointments,name='update_appts')
]