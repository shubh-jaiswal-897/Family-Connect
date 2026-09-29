from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'dashboard/index.html'

class ParentDashboardView(TemplateView):
    template_name = 'dashboard/parent.html'

class ChildDashboardView(TemplateView):
    template_name = 'dashboard/child.html'
