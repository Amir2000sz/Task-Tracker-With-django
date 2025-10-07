from django.urls import path
from .views import getUsers,displayUser,editTask,deleteTask
urlpatterns = [path("dashboard/",getUsers,name="dashboard"),
               path("user/<int:pk>",displayUser,name="displayUser"),
               path("task/<int:pk>/edit",editTask,name="editTask"),
               path("task/<int:pk>/delete",deleteTask,name="deleteTask"),]