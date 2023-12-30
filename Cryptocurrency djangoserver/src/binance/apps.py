from django.apps import AppConfig


class BinanceConfig(AppConfig):
    name = 'binance'

class ElasticsearchappConfig(AppConfig):
    name = 'binance'

    def ready(self):
        import binance.signals
