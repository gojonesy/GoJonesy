from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from blog.models import Post
from blog.forms import PostForm

# Create your views here.
def posts_list(request):
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 25) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render(request, "blog/list.html", context)


def posts_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, instance.title + " created.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, "blog/post_form.html", context)

def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        'title': instance.title,
    }
    return render(request, "blog/post_detail.html", context)

def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, instance.title + " saved.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'content': instance.content,
        'form': form,
    }
    return render(request, "blog/post_form.html", context)

def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, instance.title + " deleted.")

    return redirect("blog-index")
