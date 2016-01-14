from django.shortcuts import render,redirect, get_object_or_404
from .forms import UserForm, CommentForm
from .models import Comment, Story
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    stories = Story.objects.all()
    return render(request,"index.html",{'stories':stories})

def check(request):
    if request.method == 'POST':
        story = get_object_or_404(Story,pk=request.POST['story_pk'])
        if request.POST.get('passed')=="False":
            story.passed = False
        elif request.POST.get('passed')=="True":
            story.passed = True
        story.checked = True
        story.save()
    stories = Story.objects.filter(checked=False).order_by("published_date")
    if stories:
        story = stories[0]
    else:
        story = None
    return render(request,"check.html",{'story':story})

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,'register.html',{'user_form': user_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('qb.views.index')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request,"login.html")
    else:
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('qb.views.index')

def comment(request, pk):
    comment_form = CommentForm(request.POST or None)
    story = get_object_or_404(Story, pk=pk)
    if request.method == 'POST' and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.story = story
        comment.save()
        return redirect('qb.views.comment',pk=pk)
    comments = Comment.objects.filter(story__pk=pk)
    return render(request, 'comment.html', {'story': story,'comments':comments})

def profile(request):
    stories = Story.objects.filter(user=request.user)
    comments = Comment.objects.filter(user=request.user)
    return render(request, 'profile.html', {'stories': stories,'comments':comments})

@login_required(login_url='/login/')
def publish(request):
    published = False
    if request.method == 'POST':
        story = Story(user=request.user,context=request.POST['story'])
        story.save()
        published = True
    return render(request,"publish.html",{'published':published})







