from django.shortcuts import render
from fetch import elements
# Create your views here.
def down(request):
	element = elements()
	return render(request,'index.html',{'elements':element})