from django.db import models
from devices.models import ChildDevice
from accounts.models import User

class ScreenSession(models.Model):
    child_device = models.ForeignKey(ChildDevice, on_delete=models.CASCADE)
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='requested')
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    child_consent = models.BooleanField(default=False)
