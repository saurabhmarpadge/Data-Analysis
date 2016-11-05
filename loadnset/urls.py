from django.conf.urls import url
from django.views.generic import TemplateView

app_name = 'loadnset'
urlpatterns = [
            url(r'^index/', TemplateView.as_view(template_name='index.html'), name='index'),
            url(r'^about/', TemplateView.as_view(template_name ='about.html'), name='about')
        ]
