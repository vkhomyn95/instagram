# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'user')
