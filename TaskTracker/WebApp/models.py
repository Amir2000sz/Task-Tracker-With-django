from django.db import models

class UserCustom(models.Model):
    DisplayName = models.CharField(max_length=200,unique=True)
    email = models.CharField(max_length=100,unique = True)
    Name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    addedDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)
    password = models.CharField(null=False,blank=False)
    def __str__(self):
        return self.DisplayName

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(UserCustom,on_delete=models.CASCADE,related_name="tasks")
    title = models.TextField()
    isDone = models.BooleanField(default=False)
    addedDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

