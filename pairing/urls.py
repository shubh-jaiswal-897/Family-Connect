from django.urls import path
from pairing.views import CreatePairingQRView

urlpatterns = [
    path('create/', CreatePairingQRView.as_view(), name='create_pairing'),
]
