from django.contrib.auth import login
from django.forms import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm



def projects(request):
    '''This method will return the view for all projects'''

    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html',context)


def project(request,pk):
    '''This method will return the view for single-project'''

    projectObj = Project.objects.get(id = pk)
    
    return render(request, 'projects/single-project.html', {'project':projectObj })


@login_required(login_url="login")
def createProject(request):
    '''This method will create a new project'''

    form = ProjectForm()

    if(request.method == 'POST'):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, "projects/project_form.html",context)



@login_required(login_url="login")
def updateProject(request,pk):
    '''This method will update project'''

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if(request.method == 'POST'):
        form = ProjectForm(request.POST,request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}

    return render(request, "projects/project_form.html",context)




@login_required(login_url="login")
def deleteProject(request,pk):
    '''This method will delete a project by its ID'''

    project = Project.objects.get(id=pk)

    if(request.method == 'POST'):
        project.delete()
        return redirect('projects')

    context = {'object':project}

    return render(request, 'projects/delete_template.html',context)