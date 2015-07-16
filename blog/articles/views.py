from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Articles

class IndexView(generic.ListView):
    template_name = 'articles/index.html'

    def get_queryset(self):
        return Articles.objects.filter