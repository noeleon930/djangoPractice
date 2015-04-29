from datetime import datetime
from django.shortcuts import render
from noel.models import Post
import numberrr


def hello_world(request):
    a = numberrr.mulmul(1000000000)
    return render(request, 'hello_world.html', {'current_time': datetime.now(), 'number': a})


def home(request):
    # get all the posts
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list': post_list})
