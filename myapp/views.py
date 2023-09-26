from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    #return HttpResponse("<h2>Pagina Inicial</h2>")
    return render(request, "index.html")

def saludo(request, username):    
    return HttpResponse("<h2>Saludo %s desde la vista principal!...</h2>" % username)

def acerca(request):
    return HttpResponse("<h3>Acerca de ...</h3>")

def proyectos(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, "proyectos.html", {'projects':projects}) 

def tareas(request, id):
    # task = Task.objects.get(id=id) Sin el get_object_or_404
    task = get_object_or_404(Task, id=id)
    return HttpResponse("Tarea: %s" % task.title)

def ttareas(request):
    tasks=Task.objects.all()
    print(tasks)
    return render(request, "tareas.html", {'tasks':tasks})

def nuevatarea(request):
    if request.method == 'GET':
        # Mostrar codigo con GET
        return render(request, "newtask.html", {'form': CreateNewTask})
    else:
        # Mostrar codigo con POST
        Task.objects.create(title=request.POST['title'])
        description=request.POST['desription'], project_id=1
        return redirect('tasks')

def nuevoproyecto(request):
    if request.method == 'GET':
        return render(request,"newproject.html", {'form': CreateNewProject})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def detalleproyecto(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "pdetail.html", {'project':project, 'tasks':tasks})