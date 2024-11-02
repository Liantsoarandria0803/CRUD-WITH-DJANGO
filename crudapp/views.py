from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def index(request):
    todos=Todo.objects.all()
    return render(request ,'index.html',{'todos':todos,})
def addTasks(request):
    if request.method == 'POST':
        name=request.POST.get('task')
        Todo.objects.create(name=name)
        return redirect('index')
    else:
        return  redirect('index')
def updateTaskForm(request,pk):
    todo=Todo.objects.get(id=pk)
    return render(request,'update.html',{'todo':todo})
def deleteTask(request,pk):
    todo=Todo.objects.get(id=pk)
    todo.delete()
    return redirect('index')
def updateTask(request,pk):
    todo=Todo.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('task')
        if name:
            todo.name = name
            todo.save()
            return redirect('index')
    return redirect('updateTaskForm', pk=pk)