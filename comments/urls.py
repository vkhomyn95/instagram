from django.conf.urls import url

from comments.views import CommentCreateView
#from photos.views import UserListView

urlpatterns = [
    url(r'^upload-photo2/$', CommentCreateView.as_view(), name='add'),
    # url(r'^upload-photo3/$', UserListView.as_view(), name='a'),
]
