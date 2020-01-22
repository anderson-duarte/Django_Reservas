import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    registrado_em = models.DateTimeField('data do registro')

    def reservas_nao_confirmadas(self):
        return self.reserva_set.filter(confirmada=False)


    def reservas_confirmadas(self):
        return self.reserva_set.filter(confirmada=True)


    def __str__(self):
        return self.nome

    def registro_eh_antigo(self):
        um_ano = timezone.now() - datetime.timedelta(days=365)
        return self.registrado_em < um_ano

    registro_eh_antigo.admin_order_field = 'registrado em'
    registro_eh_antigo.boolean = True
    registro_eh_antigo.short_description = 'Cliente Antigo?'




class Reservas(models.Model):
    data_reserva = models.DateTimeField('data da reserva')
    data_evento = models.DateTimeField('data do evento')
    pessoas = models.IntegerField(default=0)
    confirmada = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=type)

    def __str__(self):
        return '{} - {}'.format(self.cliente, str(self.data_evento))
