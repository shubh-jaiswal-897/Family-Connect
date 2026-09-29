from django.db import models
from devices.models import ChildDevice

class Permission(models.Model):
    PERMISSION_TYPES = (
        ('DEVICE_PAIRING', 'Device Pairing'),
        ('FILE_SHARING', 'File Sharing'),
        ('SCREEN_SHARING', 'Screen Sharing'),
        ('CAMERA', 'Camera'),
        ('MICROPHONE', 'Microphone'),
        ('LOCATION', 'Location'),
    )
    STATUS_CHOICES = (
        ('ALLOWED', 'Allowed'),
        ('DENIED', 'Denied'),
        ('PENDING', 'Pending'),
    )
    child_device = models.ForeignKey(ChildDevice, on_delete=models.CASCADE, related_name='permissions')
    permission_type = models.CharField(max_length=50, choices=PERMISSION_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    granted_at = models.DateTimeField(null=True, blank=True)
    revoked_at = models.DateTimeField(null=True, blank=True)
