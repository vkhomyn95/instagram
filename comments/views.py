# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from comments.models import Comment


class CommentView(ListView):

    model = Comment
    context_object_name = 'comments'
    template_name = 'comments.html'
