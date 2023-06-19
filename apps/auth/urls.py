from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import TokenPairView, CheckUserAndGetEmailForRecovery, RecoveryPassword

urlpatterns = [
    path('', TokenPairView.as_view(), name='token_obtain_pair'),
    path('/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/recovery', CheckUserAndGetEmailForRecovery.as_view(), name='get_email_for_password'),
    path('/recovery/<str:token>', RecoveryPassword.as_view(), name='recovery_password'),
]
