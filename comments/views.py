# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from comments.forms import AddCommentForm
from comments.models import Comment


class CommentView(ListView):

    model = Comment
    context_object_name = 'comments'
    template_name = 'comments.html'


class CommentCreateView(CreateView):

    form_class = AddCommentForm
    model = Comment
    template_name = 'addcomment.html'
    redirect_field_name = 'photo_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(CommentCreateView, self).form_valid(form)


@login_required
def add_new_comment_to_photo(request):
    form = AddCommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
        return JsonResponse({'success': True, 'user': request.user.username, 'text': comment.text})
    else:
        return JsonResponse({'errors': form.errors}, status=400)
