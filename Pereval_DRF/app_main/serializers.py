from rest_framework import serializers

from .models import PerevalAdd


class PerevalAddSerializer(serializers.ModelSerializer):
    """Сериализатор перевалов"""
    class Meta:
        model = PerevalAdd