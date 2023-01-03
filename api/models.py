from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    description = models.CharField(max_length=512)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.description
