from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from .models import Task    

# Create your views here.
def addTask(request):
    if request.method == 'POST':
        newTask = request.POST['task']
        if newTask != '':
            taskExists = Task.objects.filter(task = newTask)
            if taskExists:
                return HttpResponse("Task already exists")  
            Task.objects.create(task = newTask)
        else:
            return HttpResponse("You must enter a task")

    return redirect('home') 


def markAsDone(request, pk):
    taskUpdated = get_object_or_404(Task, pk=pk)
    taskUpdated.isCompleted = True
    taskUpdated.save()

    return redirect('home')


def markAsUnDone(request, pk):
    taskUpdated = get_object_or_404(Task, pk=pk)
    taskUpdated.isCompleted = False
    taskUpdated.save()

    return redirect('home')

def editTask(request, pk):
    getTask = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        updatedTask = request.POST['task']
        if updatedTask != '':
            getTask.task = updatedTask
            getTask.save()
            return redirect('home')
        else:
            return HttpResponse("You must enter a task")
    context = {
        'getTask': getTask,
    }
    return render(request, 'editTask.html',context)


def deleteTask(request, pk):
    taskDeleted = get_object_or_404(Task, pk=pk)
    taskDeleted.delete()

    return redirect('home')

