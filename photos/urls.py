from django.conf.urls import url

from comments.views import CommentView
from photos.views import PhotoView, PhotoDetailView, AddPhotoView

urlpatterns = [
    url(r'^$', PhotoView.as_view(), name='photo'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail'),
    url(r'^upload-photo/$', AddPhotoView.as_view(), name='add_photo'),
    url(r'^photo/bla/$', CommentView.as_view(), name='bla'),
]
