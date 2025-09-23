from django.apps import AppConfig


class Config(AppConfig):
    """
    AppConfig for django-notification-system.
    
    This configuration class defines the app metadata for the Django notification system.
    The name attribute must match the app's module name for proper Django integration.
    """
    name = "django_notification_system"
    default_auto_field = 'django.db.models.BigAutoField'
