from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import MainDonate, DonationDonate, ProjectDonate, ProjectsDonate, FooterDonate
from .serializers import (
    MainDonateSerializer,
    DonationDonateSerializer,
    ProjectDonateSerializer,
    ProjectsDonateSerializer,
    FooterDonateSerializer,
)


class MainDonateViewSet(ModelViewSet):
    queryset = MainDonate.objects.all()
    serializer_class = MainDonateSerializer
    permission_classes = [IsAuthenticated]


class DonationDonateViewSet(ModelViewSet):
    queryset = DonationDonate.objects.all()
    serializer_class = DonationDonateSerializer
    permission_classes = [IsAuthenticated]


class ProjectDonateViewSet(ModelViewSet):
    queryset = ProjectDonate.objects.all()
    serializer_class = ProjectDonateSerializer
    permission_classes = [IsAuthenticated]


class ProjectsDonateViewSet(ModelViewSet):
    queryset = ProjectsDonate.objects.all()
    serializer_class = ProjectsDonateSerializer
    permission_classes = [IsAuthenticated]


class FooterDonateViewSet(ModelViewSet):
    queryset = FooterDonate.objects.all()
    serializer_class = FooterDonateSerializer
    permission_classes = [IsAuthenticated]
