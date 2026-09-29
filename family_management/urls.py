from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/pairing/', include('pairing.urls')),
]
