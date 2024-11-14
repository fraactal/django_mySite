from django.db import models

# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    # este campo tiene unarelación con la otra tabla proyecto
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # si elimino un proyecto, se eliminarán las tareas
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + '  |  ' + self.project.name
