from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from planner_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange

def user_signup(request):
	if request.method == "POST":
		un = request.POST.get("un")
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username = un)
			return render(request, "user_signup.html", {"msg":"Username already registered!!"})
		except User.DoesNotExist:
			try:
				usr = User.objects.get(email = em)
				return render(request, "user_signup.html", {"msg":"Email already registered!!"})
			except User.DoesNotExist:
				pw = ""
				text = "ABCDEFGHJKLMNPQRSTUVWXYZ123456789abcdefghijkmnopqrstuvwxyz"
				for i in range(6):
					pw = pw + text[randrange(len(text))]
				print(pw)
				msg = "Hello " + un + "\nWelcome to Planner by Shubham" + "\nYour username is "+ un +"\nYour Password is " + pw
				send_mail("Welcome to Planner by Shubham", msg, EMAIL_HOST_USER, [str(em)])
				usr = User.objects.create_user(username=un, password=pw, email=em)
				usr.save()
				return redirect("user_login")
	else:
		return render(request, "user_signup.html")

def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un, password=pw)
		if usr is None:
			return render(request, "user_login.html", {'msg':"Invalid Credentials!"})
		else:
			login(request, usr)
			return redirect("home")
	else:
		return render(request, "user_login.html")

def user_logout(request):
	logout(request)
	return redirect("user_login")

def user_fp(request):
	if request.method == "POST":
		un = request.POST.get("un")
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username = un) and User.objects.get(email = em)
			pw = ""
			text = "ABCDEFGHJKLMNPQRSTUVWXYZ123456789abcdefghijkmnopqrstuvwxyz"
			for i in range(6):
				pw = pw + text[randrange(len(text))]
			print(pw)
			msg = "Hello " + un + "\nWelcome to Planner by Shubham" + "\nYour username is "+ un +"\nYour New Password is " + pw
			send_mail("Welcome to Planner by Shubham", msg, EMAIL_HOST_USER, [str(em)])
			usr.set_password(pw)
			usr.save()
			return redirect("user_login")
		except User.DoesNotExist:
			return render(request, "user_fp.html", {'msg':"Invalid Info!!"})
	else:
		return render(request, "user_fp.html")

def user_cp(request):
	if request.method == "POST" and request.user.is_authenticated:
		un = request.user.username
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		if pw1 == pw2:
			usr = User.objects.get(username = un)
			usr.set_password(pw1)
			usr.save()
			return redirect("user_login")
		else:
			return render(request, "user_cp.html", {'msg':'Password did not match!!'})	
	elif request.method == "GET" and request.user.is_authenticated:
		return render(request, "user_cp.html")
	else:
		return redirect("user_login")







