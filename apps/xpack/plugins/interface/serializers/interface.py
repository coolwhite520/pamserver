from django.db import transaction
from rest_framework import serializers

from ..models import Interface


class InterfaceSerializer(serializers.Serializer):
    login_title = serializers.CharField(required=False, max_length=128)
    login_image = serializers.ImageField(required=False)
    favicon = serializers.ImageField(required=False)
    logo_index = serializers.ImageField(required=False)
    logo_logout = serializers.ImageField(required=False)

    def create(self, validated_data):
        return self.update_validated_interface(validated_data)

    def update(self, instance, validated_data):
        return self.update_validated_interface(validated_data, instance)

    def update_validated_interface(self, validated_data, instance=None):
        if not instance:
            instance = Interface()
        with transaction.atomic():
            for name, value in validated_data.items():
                if not value:
                    continue
                setattr(instance, name, value)
            instance.save()
        return instance
