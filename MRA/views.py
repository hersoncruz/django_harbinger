from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import *

class IndexView(generic.ListView):
    model = Employee
    template_name = 'MRA/index.html'
    context_object_name = 'employee_list'

    def get_queryset(self):
        return Employee.objects.all()
