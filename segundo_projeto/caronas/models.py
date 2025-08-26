from django.db import models
from django.contrib.auth.models import User

class Status(models.TextChoices):
    ACEITA = 'ACEITA', 'Carona aceita'
    RECUSADA = 'RECUSADA', 'Carona recusada'
    PENDENTE = 'PENDENTE', 'Solicitação pendente'

class Carona(models.Model):
    motorista = models.ForeignKey(User, on_delete=models.CASCADE)
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    horario_saida = models.DateTimeField()
    assentos_disponiveis = models.IntegerField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.motorista} - {self.origem} - {self.destino} - {self.horario_saida} - {self.assentos_disponiveis} - {self.preco} - {self.observacoes}'

class SolicitacaoCarona(models.Model):
    carona = models.ForeignKey(Carona, on_delete=models.CASCADE)
    passageiro = models.ForeignKey(User, on_delete=models.CASCADE)
    data_solicitacao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Status.choices)

    def __str__(self):
        return f'{self.carona} - {self.passageiro} - {self.data_solicitacao} - {self.status}'