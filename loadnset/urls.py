from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
app_name = 'loadnset'
urlpatterns = [
            url(r'^index/', views.down, name='index'),
            url(r'^about/', TemplateView.as_view(template_name ='about.html'), name='about')
        ]
