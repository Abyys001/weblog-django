from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

# my forms
from .forms import PostForm
# my models
from .models import *


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "./posts/post_list.html", context)


class PostList(generic.ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = 'posts/post_list.html'


def post_detail(request, post_id):
    # try:
    #     post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound("<h1>Post Does NOT Exist!!</h1>")

    post = get_object_or_404(Post, pk=post_id)
    comment = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comment ": comment,
    }
    return render(request, "./posts/post_detail.html", context)


class PostDetail(generic.ListView):
    queryset = get_object_or_404(Post, pk=post_id)

    context_object_name = 'post', 'comment'
    template_name = './posts/post_detail.html'


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts')
    else:
        form = PostForm()

    return render(request, './posts/post_create.html', {'form': form})