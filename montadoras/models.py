from django.db import models


class Montadora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    ano_fundacao = models.IntegerField()

    def __str__(self):
        return self.nome


class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    valor_referencia = models.DecimalField(max_digits=10, decimal_places=2)
    motorizacao = models.CharField(max_length=10)
    turbo = models.BooleanField(default=False)
    automatico = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.CharField(max_length=50)
    ano_fabricacao = models.IntegerField()
    ano_modelo = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    placa = models.CharField(max_length=7, unique=True)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
