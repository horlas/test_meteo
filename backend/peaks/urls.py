from .views import PeakViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'peaks'

router = DefaultRouter()
router.register(r'peaks', PeakViewSet, basename='peak')
urlpatterns = router.urls


