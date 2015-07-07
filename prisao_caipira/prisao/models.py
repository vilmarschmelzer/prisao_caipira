from django.db import models
from .manager import PrisioneiroManager


class Prisioneiro(models.Model):
    prisioneiro_id = models.IntegerField()
    is_preso = models.BooleanField(default=True)
    data = models.DateTimeField()

    objects = PrisioneiroManager()

    def __unicode__(self):
        return str(self.prisioneiro_id)