from django.db import models
from devices.models import ChildDevice

class SharedFile(models.Model):
    child_device = models.ForeignKey(ChildDevice, on_delete=models.CASCADE, related_name='shared_files')
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    file_size = models.BigIntegerField()
    consent_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
