# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView

from photos.forms import PhotoAddForm
from photos.models import Photo


class PhotoView(ListView):

    model = Photo
    context_object_name = 'photos'
    template_name = 'photos.html'


class PhotoDetailView(DetailView):

    model = Photo
    context_object_name = 'photo'
    template_name = 'photo_detail.html'


class AddPhotoView(CreateView):

    form_class = PhotoAddForm
    model = Photo
    template_name = 'upload_photo.html'
    redirect_field_name = 'photo_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPhotoView, self).form_valid(form)






