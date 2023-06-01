from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenObtainSerializer


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer

