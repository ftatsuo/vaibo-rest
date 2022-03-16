from .models import Smartphone
from rest_framework import serializers

class SmartphoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Smartphone
    fields = '__all__'