# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from photos.models import Photo, Lead

# Register your models here.

admin.site.register(Photo)
admin.site.register(Lead)