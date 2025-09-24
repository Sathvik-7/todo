from django.shortcuts import render, HttpResponse, redirect

from .models import Task    

# Create your views here.
def addTask(request):
    newTask = request.POST['task']
    Task.objects.create(task = newTask)

    return redirect('home') 