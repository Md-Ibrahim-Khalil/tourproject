from rest_framework import serializers
from .models import Agency, Tour

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ['id','name','nid_number','phone_number']
        
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
