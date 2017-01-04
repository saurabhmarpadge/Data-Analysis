from django.shortcuts import render
from . import fetch
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/auth/index")
def down(request):
	element = fetch.elements()
	return render(request,'index.html',{'elements':element})                                 