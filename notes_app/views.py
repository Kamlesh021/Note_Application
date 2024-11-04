from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from django.contrib import messages

def home(request):
	return render(request,"notes_app/home.html")

def add_task(request):
	if request.method=="POST":
		task_desc=request.POST.get("task")
		if task_desc:
			Note.objects.create(task=task_desc)
			messages.success(request,"Task added successfullly")

		else:
			messages.error(request,"Task description cannot be empty.")
		return redirect("view_tasks")
	return render(request,"notes_app/add_task.html")

def view_tasks(request):
	tasks=Note.objects.all()
	return render(request,"notes_app/view_tasks.html",{"tasks":tasks}) 

def update_tasks(request,id):
	task=get_object_or_404(task,id=id)
	if request.method=="POST":
		task_description=request.post.get("task")
		task.task=task_description
		task.save()
		return redirect("view_tasks")
	return render(request,"notes_app/view_tasks.html",{"tasks":task})

def delete_tasks(request,id):
	task=get_object_or_404(task,id=id)
	if request.method=="POST":
		task.delete()
		return redirect("view_tasks")
	return render(request,"notes_app/view_tasks.html",{"tasks":task})

