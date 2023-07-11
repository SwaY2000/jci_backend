from rest_framework import serializers
from .models import MainDonate, DonationDonate, ProjectDonate, ProjectsDonate, FooterDonate


class MainDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDonate
        fields = '__all__'

class DonationDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationDonate
        fields = '__all__'

class ProjectDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsDonate
        fields = '__all__'

class ProjectsDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsDonate
        fields = '__all__'

class FooterDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterDonate
        fields = '__all__'

