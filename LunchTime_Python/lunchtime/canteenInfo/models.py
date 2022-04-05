from django.db import models
import uuid
from userdetail.models import Profile
from django.utils import timezone


def one_day_hence():
    return timezone.localtime(timezone.now() + timezone.timedelta(minutes=30))


class CanteenInfo(models.Model):
    profile_id = models.OneToOneField(Profile, on_delete=models.CASCADE, null =True, blank=True)
    canteen_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True,)
    active_or_not = models.BooleanField()
    last_scan_date_and_time = models.DateTimeField(default=timezone.localtime(timezone.now()))
    end_time = models.TimeField(default=one_day_hence())

    def __str__(self):
        a = self.last_scan_date_and_time
        b = self.end_time
        return str(f'Start time {a} End time {b}')
