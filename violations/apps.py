from django.apps import AppConfig


class ViolationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'violations'
def ready(self):
    import violations.signals
