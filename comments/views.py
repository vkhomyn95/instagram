# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, CreateView


from comments.forms import CommentForm
from comments.models import Comment


class CommentView(ListView):

    model = Comment
    context_object_name = 'comments'
    template_name = 'comments.html'


class CommentCreateView(CreateView):

    form_class = CommentForm
    model = Comment
    template_name = 'addcomment.html'
    redirect_field_name = 'photo_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(CommentCreateView, self).form_valid(form)