from django.db import models

# Create your models here.
class CEP(models.Model):
	nome = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	cep = models.CharField(max_length=8)
	endereco = models.CharField(max_length=50)
	numero = models.CharField(max_length=10)
	bairro = models.CharField(max_length=50)
	cidade = models.CharField(max_length=30)
	uf = models.CharField(max_length=2)
	descricao = models.CharField(max_length=200)
