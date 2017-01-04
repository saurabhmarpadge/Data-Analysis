from django.views.generic import TemplateView, RedirectView
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import logout
app_name = 'authentify'
urlpatterns = [
	url(r'^index', TemplateView.as_view(template_name = 'auth.html'), name = 'loginsignup'),
	url(r'^logins/', views.logins, name = 'login'),
	url(r'^create/', views.create_account, name = 'signup'),
	url(r'^logout/', logout, {'next_page':'/auth/index'}, name="logout"),
]