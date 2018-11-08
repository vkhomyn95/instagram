from django.conf.urls import url

from comments.views import CommentCreateView
from photos.views import PhotoView, PhotoDetailView, AddPhotoView

urlpatterns = [
    url(r'^$', PhotoView.as_view(), name='photo'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail'),
    url(r'^upload-photo/$', AddPhotoView.as_view(), name='add_photo'),
    url(r'^upload-photo2/$', CommentCreateView.as_view(), name='add'),
]
