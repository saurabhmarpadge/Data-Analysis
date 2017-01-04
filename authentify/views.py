from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def logins(request):
	if request.user.is_authenticated:
		return redirect("/auth/logout/")
	username = request.POST["email"]
	password = request.POST["password"]
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect("/load/index")
	else:
		return redirect("auth/index")

def create_account(request):
	req = request.POST
	full_name = req["fullname"]
	email = req["email"]
	if User.objects.filter(username=email).exists():
		return render(request,"auth.html")
	password = req["password"]
	first_name, last_name = full_name.split(" ")
	user = User.objects.create(
			username=email, 
			first_name=first_name, 
			last_name=last_name,
			email=email)
	user.set_password(password)
	user.save()
	return redirect("/auth/index")