from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.utils import timezone

from .models import *

class IndexView(TemplateView):
    template_name = 'MRA/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['unit_list'] = Unit.objects.all()
        context['employee_list'] = Employee.objects.all()
        return context
