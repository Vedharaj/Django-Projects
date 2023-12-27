from django.db import models

# Create your models here.
class Task(models.Model):
    taskname = models.CharField(max_length=20)
    completed = models.BooleanField()
    
    def __str__(self):
        return self.task_name
    
    
    