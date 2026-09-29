from django.db import models
from accounts.models import User
import uuid
from datetime import timedelta
from django.utils import timezone

def default_expiry():
    return timezone.now() + timedelta(minutes=15)

class PairingToken(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    expires_at = models.DateTimeField(default=default_expiry)
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
