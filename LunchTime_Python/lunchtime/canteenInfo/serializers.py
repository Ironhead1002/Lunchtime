from rest_framework import serializers
from .models import CanteenInfo


class CanteenInfoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CanteenInfo
        fields = ['profile_id','last_scan_date_and_time','end_time']
