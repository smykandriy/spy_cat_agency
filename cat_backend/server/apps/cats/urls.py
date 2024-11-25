from django.urls import path, include
from rest_framework import routers

from server.apps.cats.views import (
    SpyCatViewSet,
    MissionViewSet,
    MissionTargetListAPIView,
    MissionTargetDetailAPIView,
)

router = routers.DefaultRouter()
router.register(r"cats", SpyCatViewSet, basename="cat")
router.register(r"missions", MissionViewSet, basename="mission")

urlpatterns = [
    path("", include(router.urls)),
    path("missions/<int:mission_id>/targets/", MissionTargetListAPIView.as_view()),
    path(
        "missions/<int:mission_id>/targets/<int:pk>/",
        MissionTargetDetailAPIView.as_view(),
    ),
]
