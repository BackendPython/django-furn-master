from django.apps import AppConfig


class FurnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'furn'
    
    def ready(self):
        import furn.signal
