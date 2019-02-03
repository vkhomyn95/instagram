# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView
from comments.forms import AddCommentForm
from comments.models import Comment
from photos.models import Photo


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comment'

    def get_context_data(self, pk):
        self.object = Photo.objects.get(pk=self.pk)
        return super(CommentListView, self).get_context_data(post=self.object)

    def get_queryset(self):
        return super(CommentListView, self).get_queryset().filter(post=self.object)

# class CommentListView(ListView):
#     model = Comment
#     template_name = 'comments.html'
#     paginate_by = 5
#
#     def get_context_data(self, **kwargs):
#         context = super(CommentListView, self).get_context_data(**kwargs)
#         list_comment = Comment.objects.select_related().all()
#         paginator = Paginator(list_comment, self.paginate_by)
#         page = self.request.GET.get('page')
#
#         try:
#             file_comments = paginator.page(page)
#         except PageNotAnInteger:
#             file_comments = paginator.page(1)
#         except EmptyPage:
#             file_comments = paginator.page(paginator.num_pages)
#         context['list_comments'] = file_comments
#         return context


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
