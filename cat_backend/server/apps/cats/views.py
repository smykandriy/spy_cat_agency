from rest_framework import viewsets, generics

from server.apps.cats.models import SpyCat, Mission, Target
from server.apps.cats.serializers import (
    SpyCatSerializer,
    MissionSerializer,
    TargetSerializer,
)


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionTargetListAPIView(generics.ListAPIView):
    serializer_class = TargetSerializer

    def get_queryset(self):
        mission_id = self.kwargs["mission_id"]
        return Target.objects.filter(mission__id=mission_id)


class MissionTargetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def get_object(self):
        mission_id = self.kwargs["mission_id"]
        target_id = self.kwargs["pk"]
        return Target.objects.get(id=target_id, mission__id=mission_id)
