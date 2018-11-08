# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin, ModelFormMixin

from comments.forms import CommentForm
from comments.models import Comment
from photos.models import Photo


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