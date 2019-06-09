# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core import paginator
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db.models import ProtectedError
from django.http import JsonResponse, Http404, HttpResponse, request
from django.shortcuts import get_object_or_404, redirect, render_to_response, render
from django.template import RequestContext, loader
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from comments.forms import AddCommentForm
from comments.models import Comment
from .forms import PhotoAddForm
from .models import Photo
from taggit.models import Tag


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PhotoView(TagMixin, ListView):

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


@login_required
def photo_delete_view(request, pk=None):
    photo = get_object_or_404(Photo, pk=pk)
    try:
        if request.user == photo.user:
            photo.delete()
            return redirect('photo')
        else:
            return HttpResponse('You can not delete this photo . You are not owner')
    except ProtectedError:
        return redirect('photo')


class PhotoDetailView(DetailView):

    queryset = Photo.objects.select_related('user').prefetch_related('comments', 'comments__user', 'likes')
    context_object_name = 'photo'
    template_name = 'photo_detail.html'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        comments = self.object.comments.all()
        context['comments'] = comments
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


class TagIndexView(TagMixin, ListView):
    template_name = 'photos.html'
    model = Photo
    context_object_name = 'photos'
    paginate_by = 10

    def get_queryset(self):
        return Photo.objects.filter(tags__slug=self.kwargs.get('slug'))


# def lazy_load_posts(request):
#     try:
#         post = Photo.objects.get(pk=request.POST.get('photo_id'))
#     except Photo.DoesNotExist:
#         return JsonResponse({'errors': 'Invalid photo id'}, status=400)
#     page = request.POST.get('page')
#     comments = Comment.objects.filter(post=post).values_list('id', flat=True)
#     results_per_page = 5
#     paginator = Paginator(comments, results_per_page)
#     try:
#         comments = paginator.page(page)
#     except PageNotAnInteger:
#         comments = paginator.page(2)
#     except EmptyPage:
#         comments = paginator.page(paginator.num_pages)
#     posts_html = loader.render_to_string(
#         'comments.html',
#         {'comments': comments}
#     )
#     output_data = {
#         'photo_id': request.POST.get('photo_id'),
#         'posts_html': posts_html,
#         'has_next': comments.has_next(),
#     }
#     if request.is_ajax():
#         return JsonResponse(output_data)
#     else:
#         raise Http404




