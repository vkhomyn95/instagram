# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseForbidden
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


class PhotoDetailView(FormMixin, DetailView):

    model = Photo
    context_object_name = 'photo'
    template_name = 'photo_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.post_id = self.kwargs['pk']
        f.save()
        return super(PhotoDetailView, self).form_valid(form)


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

