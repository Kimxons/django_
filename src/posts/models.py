# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.urls import reverse

class Post(models.Model):
	auther = models.ForeignKey('auther.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=False)

def __unicode__(self):
	return self.title
    
def __str__(self):
    return self.title

	
def code(self):
	return self.content[:10] +'...........'
	
def get_absolute_url(self):
	return reverse("post:detail", kwargs={"id": self.id}) 

def publish(self):
    self.published_date = timezone.now()
    self.save()