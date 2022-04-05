from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Menu(models.Model):
    # review_id = models.ForeignKey(Reviews, on_delete=models.CASCADE, null =True, blank=True)
    food_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    menu = models.CharField(max_length=500)
    latest_date = models.DateField(auto_now_add=True)  # shows the menu of current date

    def __str__(self):
        a = str(self.latest_date)
        return str(f"{self.menu} {a}")
