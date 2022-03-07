from django.shortcuts import render, redirect

def home(request):
	if request.user.is_authenticated:
		return render(request, "planner.html")
	else:
		return render(request, "home.html")
