# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def instagram(request):
    return render(request, 'instagram.html')