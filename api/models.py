# api/models.py

from django.contrib.gis.db import models

class PointData(models.Model):
    """A model to store named geographic points."""
    name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return self.name

class PolygonData(models.Model):
    """A model to store named geographic areas (polygons)."""
    name = models.CharField(max_length=100)
    area = models.PolygonField()

    def __str__(self):
        return self.name
