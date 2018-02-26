from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List",
    }
    return render(request, "blog/index.html", context)

def posts_create(request):
    context = {
        'title': "Create",
    }
    return render(request, "blog/index.html", context)

def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        'title': instance.title,
    }
    return render(request, "blog/post_detail.html", context)

def posts_update(request):
    context = {
        'title': "Update",
    }
    return render(request, "blog/index.html", context)

def posts_delete(request):
    context = {
        'title': "Delete",
    }
    return render(request, "blog/index.html", context)
