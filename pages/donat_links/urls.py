from django.urls import path

from .views import MainDonateViewSet, DonationDonateViewSet, ProjectDonateViewSet, ProjectsDonateViewSet, \
    FooterDonateViewSet

urlpatterns = [
    path('main-donate/', MainDonateViewSet.as_view({'get': 'list', 'post': 'create'}), name='main-donate'),
    path('main-donate/<int:pk>/',
         MainDonateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='main-donate-detail'),

    path('donation/', DonationDonateViewSet.as_view({'get': 'list', 'post': 'create'}), name='donation'),
    path('donation/<int:pk>/', DonationDonateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='donation-detail'),

    path('project-donate/', ProjectDonateViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-donate'),
    path('project-donate/<int:pk>/',
         ProjectDonateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='project-donate-detail'),

    path('projects-donate/', ProjectsDonateViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='projects-donate'),
    path('projects-donate/<int:pk>/',
         ProjectsDonateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='projects-donate-detail'),

    path('footer-donate/', FooterDonateViewSet.as_view({'get': 'list', 'post': 'create'}), name='footer-donate'),
    path('footer-donate/<int:pk>/',
         FooterDonateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='partners-detail'),
]
