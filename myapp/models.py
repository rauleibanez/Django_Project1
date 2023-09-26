from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    # Muestra los nombres en el panel administrador en vez de 
    # nomenclaturas de objetos
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # Muestra los titulos en el panel administrador en vez de 
    # nomenclaturas de objetos
    def __str__(self):
        return self.title + " - " + self.project.name
