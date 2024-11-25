from rest_framework import serializers
import requests
from rest_framework.exceptions import ValidationError

from server.apps.cats.models import SpyCat, Mission
from server.apps.cats.models import Target


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = (
            "id",
            "name",
            "years_of_experience",
            "breed",
            "salary",
        )

    def validate_breed(self, value):
        response = requests.get(f"https://api.thecatapi.com/v1/breeds/search?q={value}")
        if not response.json():
            raise serializers.ValidationError("Invalid breed")
        return value

    def update(self, instance, validated_data):
        instance.salary = validated_data.get("salary", instance.salary)
        instance.save()
        return instance


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = (
            "id",
            "name",
            "country",
            "notes",
            "complete",
        )

    def update(self, instance, validated_data):
        if instance.complete:
            raise ValidationError("Cannot update notes for a completed target.")
        instance.notes = validated_data.get("notes", instance.notes)
        instance.complete = validated_data.get("complete", instance.complete)
        instance.save()
        return instance


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = (
            "id",
            "cat",
            "targets",
            "complete",
        )

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            target = Target.objects.create(mission=mission, **target_data)
        mission.targets.set(Target.objects.filter(mission=mission))
        return mission
