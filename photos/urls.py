from django.conf.urls import url
from django.contrib.auth.views import login, logout

from home import views
from photos.views import PhotoView

urlpatterns = [
    url(r'^$', PhotoView.as_view(), name='photo'),
]
