from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def index(request):
    title= 'Django course!!!!'
    #Se puede pasar un parametro al html
    return render(request, 'index.html',
                  {'title':title} )


def about(request):
    username = 'Jonas'
    return render(request, 'about.html', {
        "username":username
    })
    #return HttpResponse("<h1>About</h1>")



def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1> " %username)
    #return HttpResponse("Hello World", 200)


def projects(request):
    # Obtenemos los proyectos guardados en Database
    #p = list(Project.objects.all())

    #convertimos la respuesta a un lista y obtenemos los valores de la coleccion de objetos
    #p = list(Project.objects.values())


    p = list(Project.objects.all())
    return render(request, 'projects/projects.html', {
        'projects' : p
    })
    #return JsonResponse(p, safe=False)
    #return HttpResponse("projects")



#def tasks(request, title):
def tasks(request):
    # Obtenemos la tarea por el campo id
    #task = Task.objects.get(id=id)

    #Obtenemos tarea con control de error proporcionado por django
    #task= get_object_or_404(Task, id=id)
    #task= get_object_or_404(Task, title=title)

    #tasks = Task.objects.values()

    ## trae todos los datos del listado task de base de datos 
    tasks = list(Task.objects.all())

    return render(request, 'tasks/tasks.html', {
        'tasks' : tasks
    })

def create_task(request):
    #print(request.GET) # imprime los valores modo lista
    #print(request.GET['title'])
    #print(request.GET['descripcion'])
    
    if request.method == 'GET':
        #show interface
        return render(request, 'tasks/create_task.html', {
            'form' : CreateNewTask
        })
    else:
        #Guardar registro en BaseDatos
        Task.objects.create(
            title=request.POST['title'],
            descripcion=request.POST['descripcion'],
            project_id=2)  #nombre del campo task referenciado a id_projecto
        #return redirect ('/tasks/') # desde la ruta inicial me enviarás a la ruta "task"
        return redirect ('tasks') # se agrega el nombre de la redirección segpun los patrones de url definidos en urls.py

def create_project(request):
    if request.method=='GET':
        return render(request, 'projects/create_project.html',{
        #return render(request, 'url (create_project)',{
            'form' : CreateNewProject 
        })
    else:
        #project = Project.objects.create(name = request.POST['name'])
        #print(project)

        Project.objects.create(name = request.POST['name'])
        return redirect('projects')
        #return render(request, 'projects/create_project.html',{
        #    'form' : CreateNewProject
        #}) 

# crear ruta para ver un unico proyecto
def project_details(request, id):
    #Controlamos el error de no encontrado
    project= get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project' : project,
        'tasks' : tasks
    })