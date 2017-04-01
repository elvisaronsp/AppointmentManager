from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$',views.login,name='login'),
	url(r'^appointments/(?P<date>)/$',views.appointments,name='appointments'),
	url(r'^new_appointment/$',views.new_appointment,name='new_appointments'),
	url(r'^cancel_appointment/$',views.cancel_appointment,name='cancel_appointment'),
	url(r'^doctor_details/$',views.doctor_details,name='doctor_details')
]