# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from photos.models import Photo


class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Photo, related_name='comments')
    text = models.TextField(max_length=160)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)



