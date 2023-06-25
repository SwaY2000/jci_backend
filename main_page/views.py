from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import FieldModel
from .serializers import FieldModelSerializer

class FieldModelViewSet(ModelViewSet):
    queryset = FieldModel.objects.all()
    serializer_class = FieldModelSerializer
    permission_classes = [IsAuthenticated]
