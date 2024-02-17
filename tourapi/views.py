from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from .models import Agency, Tour
from .serializers import AgencySerializer, TourSerializer

# Create API
class AgencyCreate(APIView):
    def post(self, request):        
        agency_name = len(request.data["name"])
        agency_phone = len(request.data["phone_number"])
        
        if agency_name < 5 or agency_phone != 11:
            return Response({'Message': 'Name and phone number invalid'})
        else:
            serializer = AgencySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# LIST API    
class AgencyList(APIView):
    def get(self, request):
        agency = Agency.objects.all()
        serializer = AgencySerializer(agency, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#update API
class AgencyUpdate(APIView):
    def put(self, request, id):
    
        agency = get_object_or_404(Agency, id=id)
        serializer = AgencySerializer(agency, data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    