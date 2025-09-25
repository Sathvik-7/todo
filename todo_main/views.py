from django.shortcuts import render 
from todo.models import Task    

def home(request):
    tasks = Task.objects.filter(isCompleted=False).order_by('-updatedAt')
    completedTasks = Task.objects.filter(isCompleted=True).order_by('-updatedAt')

    context = {
        'tasks': tasks,
        'completedTasks': completedTasks,
        }

    return render(request,'home.html',context)