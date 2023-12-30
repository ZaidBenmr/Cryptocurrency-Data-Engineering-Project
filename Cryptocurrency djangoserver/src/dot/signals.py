from .models import Dot
from django.db.models.signals import post_save
from django.dispatch import receiver


# Signal to save each new blog post instance into ElasticSearch
@receiver(post_save, sender=Dot)
def index_post(sender, instance, **kwargs):
    print(instance)
    instance.indexing()