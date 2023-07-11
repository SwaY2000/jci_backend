from django.urls import path

from .views import AchievementsViewSet, MainBannerViewSet, MultimediaViewSet, JCIUkrainePresidentViewSet, \
    PartnerViewSet, FAQViewSet

urlpatterns = [
    path('achievements/', AchievementsViewSet.as_view({'get': 'list', 'post': 'create'}), name='achievements'),
    path('achievements/<int:pk>/',
         AchievementsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='achievements-detail'),

    path('main-banner/', MainBannerViewSet.as_view({'get': 'list', 'post': 'create'}), name='main-banner'),
    path('main-banner/<int:pk>/', MainBannerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='main-banner-detail'),

    path('multimedia/', MultimediaViewSet.as_view({'get': 'list', 'post': 'create'}), name='multimedia'),
    path('multimedia/<int:pk>/', MultimediaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='multimedia-detail'),

    path('jci-ukraine-president/', JCIUkrainePresidentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='jci-ukraine-president'),
    path('jci-ukraine-president/<int:pk>/',
         JCIUkrainePresidentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='jci-ukraine-president-detail'),

    path('partners/', PartnerViewSet.as_view({'get': 'list', 'post': 'create'}), name='partners'),
    path('partners/<int:pk>/', PartnerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='partners-detail'),

    path('faq/', FAQViewSet.as_view({'get': 'list', 'post': 'create'}), name='faq'),
    path('faq/<int:pk>/', FAQViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='faq-detail'),
]
