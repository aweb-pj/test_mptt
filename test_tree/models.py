# Create your models here.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    material = models.FileField(upload_to="materials/",null=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
