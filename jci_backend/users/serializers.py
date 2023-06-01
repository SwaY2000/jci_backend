from rest_framework import serializers


class TokenObtainSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
