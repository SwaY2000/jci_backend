from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Achievement, MainBanner, Multimedia, JCIUkrainePresident, Partner, FAQ
from .serializers import (
    AchievementsSerializer,
    MainBannerSerializer,
    MultimediaSerializer,
    JCIUkrainePresidentSerializer,
    PartnerSerializer,
    FAQSerializer,
)
from .validators import MaxUploadSizeValidator, MAX_UPLOAD_SIZE


class UploadPhotoMixin:
    @action(detail=True, methods=['post'])
    def upload_photo(self, request, pk=None):
        instance = self.get_object()
        photo = request.FILES.get('photo')

        if photo:
            # Validate file size
            photo_validator = MaxUploadSizeValidator(MAX_UPLOAD_SIZE)
            photo_validator(photo)

            instance.photo = photo
            instance.save()
            return Response({'message': 'Photo uploaded successfully'})
        else:
            return Response({'message': 'No photo uploaded'})


class AchievementsViewSet(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementsSerializer
    permission_classes = [IsAuthenticated]


class MainBannerViewSet(UploadPhotoMixin, viewsets.ModelViewSet):
    queryset = MainBanner.objects.all()
    serializer_class = MainBannerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def toggle_uk_flag(self, request, pk=None):
        banner = self.get_object()
        banner.show_ua_flag = not banner.show_ua_flag
        banner.save()
        return Response({'message': 'UA flag toggled successfully'})


class MultimediaViewSet(UploadPhotoMixin, viewsets.ModelViewSet):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer
    permission_classes = [IsAuthenticated]


class JCIUkrainePresidentViewSet(UploadPhotoMixin, viewsets.ModelViewSet):
    queryset = JCIUkrainePresident.objects.all()
    serializer_class = JCIUkrainePresidentSerializer
    permission_classes = [IsAuthenticated]


class PartnerViewSet(UploadPhotoMixin, viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def add_new_partner(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def add_new_qa(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
