from django.db import models

# Create your models here.

class Usuario(models.Model):

    class Meta:
        db_table = 'usuario'

    nome = models.CharField(max_length=150,blank=False)
    sobrenome = models.CharField(max_length=150,blank=False)
    email = models.CharField(max_length=200,blank=False,unique=True)

    def __str__(self):
        return self.email
    