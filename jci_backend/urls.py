from django.contrib import admin
from django.urls import path, include

from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='JCI_API',
        default_version='v1',
        description='About JCI',
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth', include('apps.auth.urls')),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0)),
]