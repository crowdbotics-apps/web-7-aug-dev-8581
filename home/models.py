from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    test_add_1 = models.BigIntegerField(null=True, blank=True,)
    test_add_2 = models.BigIntegerField(null=True, blank=True,)
    test_add_3 = models.BigIntegerField(null=True, blank=True,)
    test_add_4 = models.BigIntegerField(null=True, blank=True,)
    test_add_5 = models.BigIntegerField(null=True, blank=True,)
    test_add_6 = models.BigIntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
