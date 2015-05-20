from django.shortcuts import render, redirect
from django.forms.models import inlineformset_factory, modelformset_factory
from siteforms.models import ProjectForm
from projects.models import Project, Tag
from django.template import RequestContext
from django.http import HttpResponseRedirect

from hubusers.models import HubUser
from django.contrib.auth.hashers import check_password
import requests, json
import datetime
from django.db.models.signals import post_save
from actstream import action
from actstream.actions import follow, unfollow


# Create your views here.

def Project_Form(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES) 
        
        if form.is_valid() and github_create(request, form):
            form.save()
            action.send(request.user, verb='added a Project!')
            t=HubUser.objects.get(user__username__iexact='somuser')
            follow(request.user, t)
            redurl = '/' + str(request.user) + '/repos'
            
            return HttpResponseRedirect(redurl)
    else:
        form = ProjectForm()
        
    return render(request, 'add_project.html', {
            "form":form,
        }, context_instance=RequestContext(request))


def github_create(request, form):
    username = request.user.username
    user_git = HubUser.objects.get(user__username__iexact = username)
    if check_password(form.cleaned_data['github_password'], user_git.github_password):
        github_url = "https://api.github.com/" + user_git.github +"/repos"
        data = json.dumps({'name' : form.cleaned_data['name'], 'description' : form.cleaned_data['descript']})
        r = requests.post(github_url, data, auth=(user_git.github, form.cleaned_data['github_password']))
        return True
    else:
        form._errors['github_password'] = "Password incorrect"
        return False
    
def tabs(request, error=""):
    if request.method=="POST":
        var= request.POST.get("status")
        if var:
            redurl = '/search/status/'+ var
            return HttpResponseRedirect(redurl)
        var= request.POST.get("project")
        if var:
            redurl = '/search/project/'+ var
            return HttpResponseRedirect(redurl)
        var= request.POST.get("domain")
        if var:
            redurl = '/search/domain/'+ var
            return HttpResponseRedirect(redurl)
        var= request.POST.get("user")
        if var:
            redurl = '/search/user/'+ var
            return HttpResponseRedirect(redurl)
    
    return render(request, 'tabs.html', {'error': error})


def about_us_page(request):
    return render(request, 'about_us.html')
