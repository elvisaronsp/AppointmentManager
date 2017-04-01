from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$',views.login,name='login'),
	url(r'^appointments/(?P<date>)/$',views.appointments,name='appointments'),
	url(r'^new_appointment/$',views.new_appointment,name='new_appointments'),
]