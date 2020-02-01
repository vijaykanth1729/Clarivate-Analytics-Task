from django.urls import path, include
from .views import UserInfoView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api', UserInfoView)

urlpatterns = [
    path('', include(router.urls))
]
