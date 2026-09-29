from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('parent/', views.ParentDashboardView.as_view(), name='parent_dashboard'),
    path('child/', views.ChildDashboardView.as_view(), name='child_dashboard'),
]
