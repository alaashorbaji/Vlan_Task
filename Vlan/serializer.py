from rest_framework import serializers

from .models import Vlan_T

class VlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vlan_T
        fields=['Vlan_id','Name','Description']

