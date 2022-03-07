from django.shortcuts import render, redirect
from .forms import TodoForm
from django.contrib.auth.models import User
from .models import TodoModel

def add_todo(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			f = TodoForm(request.POST)
			for field in f:
				print(field.value())

			if f.is_valid():
				obj = f.save(commit=False)
				obj.user = User.objects.get(username=request.user.username)
				obj.save()
				fm = TodoForm()
				return render(request, 'add_todo.html', {'fm':fm, 'msg':'Task added successfully!'})
		else:
			fm = TodoForm()
			return render(request, 'add_todo.html', {'fm':fm})
	else:
		return redirect("user_login")

def show_todo(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			search = request.POST.get("search")
			data = TodoModel.objects.filter(user=request.user).filter(task=search)
			#for d in s_data:
			#	if d.task == search:
			#		data = d
			return render(request, "show_todo.html", {"data":data})
		else:
			data = TodoModel.objects.filter(user=request.user)
			return render(request, "show_todo.html", {"data":data})

def delete_todo(request, id, dl, ts):
	if request.user.is_authenticated:
		ds = TodoModel.objects.filter(task=id).filter(deadline=dl).filter(timestamp=ts).get()
		ds.delete()
	return redirect("show_todo")