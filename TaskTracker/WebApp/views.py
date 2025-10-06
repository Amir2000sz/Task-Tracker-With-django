from django.shortcuts import render,redirect
from .models import Task,UserCustom
from django.db.models import Count
def getUsers(requset):
    users = UserCustom.objects.all()
    tasks = UserCustom.objects.annotate(note_count=Count("tasks"))
    newList = []
    for i in range(len(users)):
        newList.append((users[i],tasks[i]))
    return render(requset , "dashboard.html",{"users":newList})

