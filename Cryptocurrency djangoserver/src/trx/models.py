from django.db import models
from datetime import datetime
from .search import TrxIndex

# Create your models here.

class Trx(models.Model) :
    date       = models.DateTimeField(default=datetime.now, blank = False)
    open       = models.DecimalField(max_digits=10, decimal_places=3,null=False)
    high       = models.DecimalField(max_digits=10, decimal_places=3,null=False)
    low        = models.DecimalField(max_digits=10, decimal_places=3,null=False)
    close      = models.DecimalField(max_digits=10, decimal_places=3,null=False)
    volume     = models.DecimalField(max_digits=15, decimal_places=3,null=False)
    #market_cap = models.DecimalField(max_digits=15, decimal_places=3,null=False,db_column='market cap')

    class Meta :
        ordering = ['-date']

    def indexing(self):
        obj = TrxIndex(
            meta={'id': self.id},
            id         = self.id,
            date       = self.date,
            open       = self.open,
            high       = self.high,
            low        = self.low,
            close      = self.close,
            volume     = self.volume,
            #market_cap = self.market_cap
        )
        obj.save()
        return obj.to_dict(include_meta=True)