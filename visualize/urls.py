from django.conf.urls import url
from django.views.generic import TemplateView

app_name = 'visualize'
urlpatterns = [
        url(r'^show/', TemplateView.as_view(template_name='show.html'), name='show'),
        ]
