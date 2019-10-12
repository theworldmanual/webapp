from django.contrib.postgres.fields import JSONField
from django.db import models


class World(models.Model):
    title = models.CharField(max_length=200)


class PageTemplate(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    data = JSONField(blank=True, null=True, default=dict)


class Page(models.Model):
    template = models.ForeignKey(
        'world.PageTemplate',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=255)
    data = JSONField(blank=True, null=True, default=dict)
    world = models.ForeignKey('world.World', on_delete=models.SET_NULL, null=True)
