from django.conf.urls import url

from comments import views
from comments.views import add_new_comment_to_photo

urlpatterns = [
    url(r'^add-comment/$', add_new_comment_to_photo, name='add_comment'),
]
