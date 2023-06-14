from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TokenPairSerializer


class TokenPairView(TokenObtainPairView):
    """
    Login
    """
    serializer_class = TokenPairSerializer
