from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):

    posts = Post.objects.order_by('-published')
    #return HttpResponse("このページは投稿のインデックスです。")
    return render(request, 'posts/index.html', {'posts':posts})
# Create your views here.

def post_detail(request, post_id):
    return render(request, 'posts/post_detail.html', {'post_id':post_id})