# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
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
    redirect_field_name = 'photos/photo_detail.html'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(CommentCreateView, self).form_valid(form)

