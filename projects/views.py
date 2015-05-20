from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


from projects.models import *
from projects.forms import *
import urllib2
import json 

def CreateTopic(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            new_topic = topic_form.save(commit=False)
            new_topic.forum = project.forum
            new_topic.save()
            return HttpResponseRedirect('/projects/%s/view/topics/' % project.id)
    else:
        topic_form = TopicForm()
    return render(request, 'forum/add_topic.html', {'topic_form': topic_form,})

def ViewTopic(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    topics = Topic.objects.filter(forum=project.forum.id)
    if request.method == 'POST':
        # delete/edit topic stuff
        pass
        
    return render(request, 'forum/view_topics.html', {'project':project, 
                                                      'topics':topics})


def Discussion(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    comments = Comment.objects.filter(parent=None)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        comment = request.POST.get('content')
        if comment_form.is_valid() or comment:
            cparent = request.POST.get('cparent')
            new_comment = Comment(content=comment)           
            cparent = request.POST.get('cparent')
            if cparent:
                cparent = Comment.objects.get(id=cparent)
                new_comment.parent = cparent
        
            new_comment.commenter = request.user.hubuser
            new_comment.topic = topic
            new_comment.save()
            return HttpResponseRedirect("")
                
    else:
        comment_form = CommentForm()
    return render(request, 'forum/discussion.html', {'topic':topic, 
                                                     'comments': comments, 
                                                     'comment_form':comment_form})

    

def ProjectDashboard(request):
    return render(request, 'dashboard.html')

def Project_Page(request, project_id):
    project = get_object_or_404(Project, id=int(project_id))
    
    return render(request, 'project_page.html', {'project': project})
    
    
def user_repo_list(request, username):
    user = HubUser.objects.get(user__username__iexact=username)
    repo_list = Project.objects.filter(owners=user)
    
    return render(request, 'repo_list.html', {'user_name': user.user,
                                              'repo_list': repo_list})


def repo_view(request, username, repo):
    user = HubUser.objects.get(user__username__iexact=username)
    project_details = Project.objects.get(name=repo, owners=user)
    github_request = urllib2.urlopen('https://api.github.com/repos/%s/%s' % (user.github, repo))
    json_data = json.loads(github_request.read())

    return render(request, 'repo_view.html', {'owner': json_data['owner']['login'],
                                              'name': json_data['name'],
                                              'description': json_data['description'],
                                              'url': json_data['url'],
                                              'created_at': json_data['created_at'],
                                              'updated_at': json_data['updated_at']
                                              })
