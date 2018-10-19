from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(
        max_length = 255,  
    )    
    def __str__(self):
        return self.nome


class Atividade(models.Model):
    tema = models.CharField(
        max_length = 255,  
    )
    palestrante = models.CharField(
        max_length = 255,
    )
    data = models.DateField()   
    ciclo = models.IntegerField()
    observacao = models.TextField(
        null = True,
        blank = True
    )

class Integrante(models.Model):
    nome = models.CharField(
        max_length = 255,
        null = False,
        blank = False    
    )
    nascimento = models.DateField(
        null = False,
        blank = False  
    )
    email = models.EmailField(
        null = False,
        blank = False  
    )
    telefone = models.CharField(
        max_length=255, 
        verbose_name=u'Telefone',                                
        default='0'
    )
    celular = models.CharField(
        max_length=255, 
        verbose_name='Celular',                                
        default='0'
    )   
    tarefa = models.ForeignKey(
        Tarefa, 
        on_delete=models.SET_NULL, 
        null=True
    )
    observacao = models.TextField(
        null = True,
        blank = True
    )
    doenca = models.TextField(
        null = True,
        blank = True
    )    