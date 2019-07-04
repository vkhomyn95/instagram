# -*- codng: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from taggit.managers import TaggableManager


class Photo(models.Model):
    img = models.ImageField(upload_to='photos/', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ('-date',)

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.img


class Lead(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    uuid = models.IntegerField(primary_key=True)
    roll_id = models.IntegerField(primary_key=True)

