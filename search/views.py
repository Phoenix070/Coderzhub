from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.models import User
from hubusers.models import HubUser
from django.http import HttpResponseRedirect

# Create your views here.
def search_by_user(request, username):
    users = HubUser.objects.filter(user__username__icontains=username) | HubUser.objects.filter(github__icontains=username)
    if users:
        user_list = []
        for user in users:
            projects = Project.objects.filter(owners=user)
            user_list.append({'username': user.user, 'github_name': user.github, 'project_count': projects.count()})
        return render(request, 'search_list.html', {'user_name': username,
                                                'user_list': user_list})
    else:
        return HttpResponseRedirect('/search_tabs/error')
    
def search_by_domain(request, language):
    projects_list = Project.objects.filter(language__icontains=language)
    if projects_list:
        return render(request, 'search_domain.html', {'language': language,
                                                  'projects_list': projects_list,
                                                  })
    else:
        return HttpResponseRedirect('/search_tabs/error')

def search_by_status(request, status):
    projects_list = Project.objects.filter(status = status)
    if projects_list:
        return render(request, 'search_status.html', {'status': status,
                                                  'projects_list': projects_list})
    else:
        return HttpResponseRedirect('/search_tabs/error')
    
def search_by_project(request, project_name):
    projects_list = Project.objects.filter(name__icontains = project_name)
    if projects_list:
        return render(request, 'search_project.html', {'project_name': project_name,
                                                   'projects_list': projects_list})
    else:
        return HttpResponseRedirect('/search_tabs/error')
    
    