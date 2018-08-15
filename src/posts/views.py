# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messsages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
        "form": form, 
	}
	return HttpResponse (request, "post_form.html", context) 
def post_slug(request):
	queryset = Post.objects.all()
	context = {
	   "title":"Slug"
	}
	return render(request,"main.html",context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
	    "title": instance.title,
	    "instance": instance,
	}
	return render(request,"post_detail.html",context) 

def post_list(request):
	posts = Post.objects.filter(timestamp=timezone.now()).order_by("timestamp")
	queryset = Post.objects.all()
	context = {
	   "title":"List"
	}
	return render(request,"posts/post_list.html",context) 

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	if request.method == "POST":
	    form = PostForm(request.POST or None, instance=instance)
	    if form.is_valid():
		    instance = form.save(commit=False)
		    instance.save()
		    messsages.success(request, "Saved")
		    return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	    "title": instance.title,
	    "instance": instance,
	    "form": form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messsages.success(request, "Successfully deleted")
	return redirect("posts_list")