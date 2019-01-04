# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from comments.forms import AddCommentForm
from .forms import PhotoAddForm
from .models import Photo


class PhotoView(ListView):

    context_object_name = 'photos'
    template_name = 'photos.html'

    def get_queryset(self):
        photos = list(
            Photo.objects.all().select_related('user').prefetch_related('likes', 'comments', 'comments__user',)
        )
        for photo in photos:
            if self.request.user in photo.likes.all():
                setattr(photo, 'is_liked_by_user', True)
        return photos


class AddPhotoView(CreateView):

    form_class = PhotoAddForm
    model = Photo
    template_name = 'upload_photo.html'
    redirect_field_name = 'photo_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPhotoView, self).form_valid(form)


class PhotoDetailView(DetailView):

    queryset = Photo.objects.select_related('user').prefetch_related('comments', 'comments__user', 'likes')
    context_object_name = 'photo'
    template_name = 'photo_detail.html'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        context['form'] = AddCommentForm(initial={'post': self.object.pk})
        context['is_liked_by_user'] = self.request.user in self.object.likes.all()
        return context


@login_required
def like_photo(request):
    try:
        photo = Photo.objects.get(pk=request.POST.get('photo_id'))
    except Photo.DoesNotExist:
        return JsonResponse({'errors': 'Invalid photo id'}, status=400)

    if photo.likes.filter(pk=request.user.pk).exists():
        is_liked = False
        photo.likes.remove(request.user)
    else:
        is_liked = True
        photo.likes.add(request.user)

    data = {
        'photo_id': request.POST.get('photo_id'),
        'is_likes': is_liked,
        'total_likes': photo.total_likes(),
        'users': [user.username for user in photo.likes.all()]
    }

    if request.is_ajax():
        return JsonResponse(data)
    else:
        raise Http404
