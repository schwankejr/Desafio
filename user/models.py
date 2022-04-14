from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):

    user_system = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf_cnpj= models.CharField(max_length=20, unique=True)
    nome_completo = models.CharField(max_length=100)
    data_nascimento= models.DateField()
    status= models.BooleanField(default=True)


    def __str__(self):
        return f'{self.user_system} -- {self.nome_completo} -- {self.cpf_cnpj}'
