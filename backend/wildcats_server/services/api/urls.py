from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
    path('services/<int:pk>/register_superuser/', ServiceViewSet.as_view({'post': 'register'}), name='register-superuser'),
]
