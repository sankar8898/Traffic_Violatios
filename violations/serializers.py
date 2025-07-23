from rest_framework import serializers
from .models import Violation
import re
import requests
from django.utils import timezone

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = '__all__'

    def validate_license_plate(self, value):
        pattern = r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Invalid Indian license plate format")
        return value

    def validate_violation_datetime(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Violation datetime cannot be in the future")
        return value

    def validate_violation_image_url(self, value):
        if not value.startswith("https://"):
            raise serializers.ValidationError("URL must be HTTPS")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        try:
            response = requests.get(value, stream=True, timeout=5, headers=headers)
            if response.status_code >= 400:
                raise serializers.ValidationError(f"Image URL returned error: {response.status_code}")

            content_type = response.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                raise serializers.ValidationError("URL does not point to an image file")

        except requests.RequestException as e:
            raise serializers.ValidationError(f"Could not connect to URL: {str(e)}")

        return value
