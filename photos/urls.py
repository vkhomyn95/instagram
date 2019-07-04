from django.conf.urls import url

from photos import views
from photos.views import PhotoView, PhotoDetailView, AddPhotoView, TagIndexView, photo_delete_view, make_new_lead, \
    make_lead_view

urlpatterns = [
    url(r'^makelead/$', make_lead_view, name='make_lead'),
    url(r'^makelead-form/$', make_new_lead, name='lead'),
    url(r'^main/$', PhotoView.as_view(), name='photo'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail'),
    url(r'^upload-photo/$', AddPhotoView.as_view(), name='add_photo'),
    url(r'^delete/(?P<pk>\d+)/$',photo_delete_view, name='delete_photo'),
    url(r'^like/$', views.like_photo, name='like_photo'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagged'),
    url(r'^lazy_load_list/$', views.lazy_load_list, name='lazy_load_list'),

]
