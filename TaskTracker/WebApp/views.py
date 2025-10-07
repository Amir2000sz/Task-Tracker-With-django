from django.shortcuts import render,redirect
from .models import Task,UserCustom
from django.db.models import Count
from django.http import Http404
from .forms import EditTaskForm
def getUsers(requset):

    users = UserCustom.objects.all()
    tasks = UserCustom.objects.annotate(task_count=Count("tasks"))
    newList = []
    for i in range(len(users)):
        newList.append((users[i],tasks[i]))
    return render(requset , "dashboard.html",{"users":newList})

def displayUser(requset , pk):
    user = UserCustom.objects.filter(pk = pk).first()
    tasks = Task.objects.filter(user = user)
    if not user :
        raise Http404("User not found")
    return render(requset,"display_user.html",{"user":user ,"tasks":tasks})

def editTask(request , pk):
    task = Task.objects.filter(pk = pk).first()
    if not task:
        raise Http404("the task not found")
    if request.method == 'POST':
        form = EditTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('displayUser', pk=task.user.id)
    else:
        # Otherwise, just display the form with the current data
        form = EditTaskForm(instance=task)
    return render(request, 'editTask.html', {'form': form, 'task': task})
    
def deleteTask(request, pk):
    task = Task.objects.filter(pk = pk).first()
    if not task:
        raise Http404("task not found")
    if request.method == "POST":
        task.delete()
        return redirect(displayUser,pk = task.user.id)
    else:
        return render(request, "deleteTask.html", {"task": task})