from django.urls import path
from .views import TokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
