from django.db import models
import uuid
from django.contrib.auth.models import User
from menu.models import Menu


class Reviews(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null =True, blank=True)
    reviews_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True,)
    menu_rev_star = models.FloatField(blank=True, null=True)
    menu_rev_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(f"{self.menu_rev_star} {self.menu_rev_comment}")
