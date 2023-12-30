from django.apps import AppConfig


class EthereumConfig(AppConfig):
    name = 'ethereum'

class ElasticsearchappConfig(AppConfig):
    name = 'ethereum'

    def ready(self):
        import ethereum.signals