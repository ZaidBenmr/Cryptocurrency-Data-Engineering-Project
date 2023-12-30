from django.apps import AppConfig


class XrpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'xrp'

class ElasticsearchappConfig(AppConfig):
    name = 'xrp'

    def ready(self):
        import xrp.signals