from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = Task.objects.all().values()
    if request.method == "POST":
        taskname = request.POST.get("taskname")
        task = Task(taskname=taskname, completed=False)
        task.save()
        return redirect('/')
    return render(request, 'index.html', {'data': data})
    
def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')

def completed(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')
    