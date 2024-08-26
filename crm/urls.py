from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, SimulationViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('simulations', SimulationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
