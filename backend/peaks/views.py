from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializers import PeaksSerializer
from .models import Peak
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.


class PeakViewSet(viewsets.ViewSet):
    ''' https://www.django-rest-framework.org/api-guide/viewsets/'''

    serializer_class = PeaksSerializer
    queryset =Peak.objects.all()

    def list(self, request):
        # todo : add query parameter to filter with boundary geographical box
        queryset = Peak.objects.all()
        serializer = PeaksSerializer(queryset, many=True)
        return Response(serializer.data)


