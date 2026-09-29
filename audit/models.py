from django.db import models
from accounts.models import User
from devices.models import ChildDevice

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    device = models.ForeignKey(ChildDevice, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
