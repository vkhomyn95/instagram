# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse_lazy

from photos.models import Photo


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Photo, related_name='comments', on_delete=models.PROTECT)
    text = models.TextField(max_length=160)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', kwargs={'pk': 1})



