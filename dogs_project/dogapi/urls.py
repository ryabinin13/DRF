from django.urls import include, path
from rest_framework import routers
from .views import DogViewSet


router = routers.SimpleRouter()
router.register(r'dogs', DogViewSet)

urlpatterns = [
    path('', include(router.urls))
]