from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def tasksView(request):
	tasks = Task.objects.all()
	form = TaskForm()

	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'tasks':tasks, 'form':form}
	return render(request, 'todolist/list.html', context)


def deleteView(request, pk):
	task = Task.objects.get(id = pk)

	if request.method == "POST":
		task.delete()
		return redirect('/')

	context = {'task':task}
	return render(request, 'todolist/delete_view.html', context)

def updateView(request, pk):
	task = Task.objects.get(id = pk)
	form = TaskForm(instance = task)

	if request.method == "POST":
		form = TaskForm(request.POST, instance = task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'task':task, 'form':form}
	return render(request, 'todolist/update_view.html', context)

# Create your views here.
