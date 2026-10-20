from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"

    def ready(self):
        from .cache_signals import register_cache_invalidation_signals

        register_cache_invalidation_signals()
