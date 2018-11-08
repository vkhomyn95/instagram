# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin, ModelFormMixin

from comments.forms import CommentForm
from comments.models import Comment
from photos.forms import PhotoAddForm
from photos.models import Photo


class PhotoView(ListView):

    model = Photo
    context_object_name = 'photos'
    template_name = 'photos.html'


class AddPhotoView(CreateView):

    form_class = PhotoAddForm
    model = Photo
    template_name = 'upload_photo.html'
    redirect_field_name = 'photo_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPhotoView, self).form_valid(form)


class PhotoDetailView(DetailView):

    model = Photo
    context_object_name = 'photo'
    template_name = 'photo_detail.html'


def like_photo(request):
    photo = get_object_or_404(Photo, id=request.POST.get('photo_id'))
    is_liked = False
    if photo.likes.filter(id=request.user.id).exists():
        photo.likes.remove(request.user)
        is_liked = False
    else:
        photo.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(photo.get_absolute_url())

#
# class UserListView(ListView):
#     model = Photo
#     template_name = 'liked_users.html'
#     context_object_name = 'users'
