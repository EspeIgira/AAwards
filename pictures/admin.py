# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin
from .models import Picture,Profile,Follow


admin.site.register(Picture)
admin.site.register(Profile)
admin.site.register(Follow)
