from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to ALX Travel App!"})

from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
