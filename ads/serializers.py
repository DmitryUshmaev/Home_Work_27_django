from rest_framework import serializers

from ads.models import ADS


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ADS
        fields = '__all__'
