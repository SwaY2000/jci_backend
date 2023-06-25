from rest_framework import serializers
from .models import FieldModel

class FieldModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldModel
        fields = ['id','support', 'helped', 'partner']