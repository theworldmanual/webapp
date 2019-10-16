from django.contrib.postgres.fields import JSONField
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class World(models.Model):
    title = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Ensure root element exists
        if not PageTreeElement.objects.filter(world=self, parent__isnull=True).exists():
            PageTreeElement.objects.create(world=self)

    def __str__(self):
        return self.title


class PageTemplate(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    data = JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return self.title


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
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Ensure root element exists
        if not PageTreeElement.objects.filter(world=self.world, page=self).exists():
            root = PageTreeElement.objects.get(world=self.world, parent__isnull=True)
            PageTreeElement.objects.create(world=self.world, page=self, parent=root)


class PageTreeElement(MPTTModel):
    # Used only for categories
    title = models.CharField(max_length=255, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # Used only for pages
    page = models.OneToOneField('world.Page', on_delete=models.SET_NULL, null=True)
    world = models.ForeignKey('world.World', on_delete=models.SET_NULL, null=True)
