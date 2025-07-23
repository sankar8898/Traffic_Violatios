# violations/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Violation

@receiver(post_save, sender=Violation)
def log_violation_created(sender, instance, created, **kwargs):
    if created:
        print(f"[LOG] New violation created: {instance.license_plate} at {instance.violation_datetime}")
