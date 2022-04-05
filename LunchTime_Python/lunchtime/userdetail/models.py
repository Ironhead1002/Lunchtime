from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null =True, blank=True)
    profile_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile_picture = models.ImageField(default="default.png")
    department = models.CharField(max_length=100,null=True, blank=True)
    trainee_or_employee = models.CharField(max_length=50,null=True, blank=True)
    employee_code = models.IntegerField(default=0000)

    def __str__(self):
        return str(f"{self.profile_id} {self.user.username}")
