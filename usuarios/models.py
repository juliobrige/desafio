from django.db import models
from django.core.validators import RegexValidator

class Grupo(models.TextChoices):
    VINGADORES = 'V', 'Vingadores'
    LIGA_DA_JUSTICA = 'LJ', 'Liga da Justiça'

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    telefone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\(\d{2}\)?\s?\d{4,5}-?\d{4}$',
            message='Número de telefone inválido.'
        )],
        help_text='Use o formato (xx) xxxx-xxxx.'
    )
    codinome = models.CharField(max_length=255, unique=True)
    grupo = models.CharField(
        max_length=255,
        choices=Grupo.choices,
        default=Grupo.LIGA_DA_JUSTICA,
        help_text='Escolha seu grupo.'
    )
