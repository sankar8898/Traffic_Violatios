from django.db import models

class Violation(models.Model):
    license_plate = models.CharField(max_length=20)
    violation_type = models.CharField(max_length=100)
    violation_datetime = models.DateTimeField()
    violation_image_url = models.URLField()  # ✅ Required
    location = models.CharField(max_length=255)  # ✅ Required
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"{self.license_plate} - {self.violation_type} at {self.violation_datetime}"
