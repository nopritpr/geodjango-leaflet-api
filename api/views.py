# api/views.py

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D # D is a shortcut for Distance

from .models import PointData, PolygonData
from .serializers import PointDataSerializer, PolygonDataSerializer

class PointDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows points to be viewed or edited.
    """

    queryset = PointData.objects.all()
    serializer_class = PointDataSerializer

    @action(detail=False, methods=['get'])
    def nearby_points(self, request):
        """
        A custom action to find points within a given radius.
        Example: /api/points/nearby_points/?lng=-74.0&lat=40.7&radius=5
        """
        try:
            lng = float(request.query_params.get('lng'))
            lat = float(request.query_params.get('lat'))
            radius_km = float(request.query_params.get('radius', 10))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid parameters. Please provide lng, lat, and an optional radius.'}, status=400)

        user_location = Point(lng, lat, srid=4326)

        # Filter points within the given radius (distance is converted to the model's unit)
        queryset = self.get_queryset().filter(
            location__distance_lte=(user_location, D(km=radius_km))
        )
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PolygonDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows polygons to be viewed or edited.
    """
    queryset = PolygonData.objects.all()
    serializer_class = PolygonDataSerializer

