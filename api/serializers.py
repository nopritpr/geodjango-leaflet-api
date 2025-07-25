# api/serializers.py

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import PointData, PolygonData

class PointDataSerializer(GeoFeatureModelSerializer):
    """A class to serialize PointData instances to GeoJSON."""
    class Meta:
        model = PointData
        geo_field = "location"
        fields = ('id', 'name')

class PolygonDataSerializer(GeoFeatureModelSerializer):
    """A class to serialize PolygonData instances to GeoJSON."""
    class Meta:
        model = PolygonData
        geo_field = "area"
        fields = ('id', 'name')
