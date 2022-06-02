from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Proprietario(models.Model):
    SEXO_CHOICES = {
        ("femenino", "Femenino"),
        ("masculino", "Masculino")
    }

    nome = models.CharField(max_length=50, null=False)
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    nif = models.CharField(max_length=12, null=False)
    sexo = models.CharField(max_length=10, null=False, choices=SEXO_CHOICES)
    profissao = models.CharField(max_length=20)
    telefone = models.CharField(max_length=12, null=False)

    def __str__(self):
        return self.nome


class Acessorio(models.Model):
    ESTADO_CHOICES = {
        ("excelente", "Excelente"),
        ("bom", "Bom"),
        ("danificado", "Danificado")
    }

    descricao = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=10, null=False, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.descricao


class Veiculo(models.Model):
    CORES_CHOICES = {
        ("azul", "Azul"),
        ("azul", "Azul"),
        ("azul", "Azul")
    }

    TIPO_CHOICES = {
        ("carro", "Carro"),
        ("moto", "Moto")
    }

    modelo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=20, null=False)
    placa = models.CharField(max_length=10, null=False)
    cor = models.CharField(max_length=50, null=False, choices=CORES_CHOICES)
    ano = models.IntegerField(null=False)
    preco = models.FloatField(null=False)
    foto_capa = models.ImageField(upload_to='images')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    acessorio = models.ManyToManyField(Acessorio)

    def __str__(self):
        return self.modelo
         