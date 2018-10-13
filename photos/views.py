# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from photos.models import Photo


class PhotoView(ListView):

    model = Photo
    context_object_name = 'photos'
    template_name = 'photos.html'


class PhotoDetailView(DetailView):

    model = Photo
    context_object_name = 'photo'
    template_name = 'photo_detail.html'
