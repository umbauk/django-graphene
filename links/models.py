from django.db import models
from django.conf import settings
from django.utils import timezone


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    # posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('links.Link', related_name='votes', on_delete=models.CASCADE)
