from rest_framework import serializers
from .models import Achievement, MainBanner, Multimedia, JCIUkrainePresident, Partner, FAQ


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'

class MultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multimedia
        fields = '__all__'

class JCIUkrainePresidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JCIUkrainePresident
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
