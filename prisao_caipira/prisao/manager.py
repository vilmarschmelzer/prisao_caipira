from django.db import models
from django.db.models import Q
from datetime import datetime, timedelta
from django.conf import settings


class PrisioneiroManager(models.Manager):

    def prender(self, prisioneiro_id):

        data_atual = datetime.now()

        prisioneiro = self.filter(data__gt=data_atual, prisioneiro_id=prisioneiro_id, is_preso=True).first()

        if prisioneiro:
            prisioneiro.data += timedelta(minutes=settings.MINUTOS_PRISAO)
        else:

            prisioneiro = self.model()
            prisioneiro.prisioneiro_id = prisioneiro_id
            prisioneiro.data = data_atual + timedelta(minutes=settings.MINUTOS_PRISAO)

        prisioneiro.save()

    def soltar(self, prisioneiro_id):

        prisioneiro = self.filter(prisioneiro_id=prisioneiro_id, is_preso=True).order_by('-data').first()
        if prisioneiro:
            prisioneiro.is_preso = False
            prisioneiro.save()
        return prisioneiro

    def get_presos(self):
        data_atual = datetime.now()
        presos = self.filter(data__gt=data_atual, is_preso=True).order_by('data').all()

        return presos

    def get_soltar_presos(self):
        data_atual = datetime.now()
        presos = self.filter(data__lte=data_atual, is_preso=True)

        return presos.all()
