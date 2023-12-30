from django.apps import AppConfig

class BitcoinConfig(AppConfig):
    name = 'bitcoin'

class ElasticsearchappConfig(AppConfig):
    name = 'bitcoin'

    def ready(self):
        import bitcoin.signals