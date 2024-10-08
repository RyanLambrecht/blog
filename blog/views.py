from django.shortcuts import render, get_object_or_404
from .models import Post

def base(request):
    posts = Post.objects.all()
    return render (request, "base.html",{"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})

# from django.views.generic import ListView
# from .models import Post
# class PostList(ListView):
#     model = Post
#     template_name = "post_list.html"