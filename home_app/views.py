from django.shortcuts import render
from blog.models import Post


def home(request):
    posts = Post.objects.all()

    return render(request, 'home_app/index.html', {'posts': posts})

def sidebar(request):
    data = {'name': 'shahab'}
    return render(request, 'includes/sidebar.html', context=data)

