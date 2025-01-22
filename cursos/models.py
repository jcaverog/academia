from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Usuario (AbstractUser):
    ROLES = (
        ('admin', 'administrador'),
        ('normal', 'Usuario Normal'),
    )

    rol = models.CharField(max_length=7, choices=ROLES, default='normal')

class curso(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupos = models.PositiveSmallIntegerField
    estado = models.BooleanField(default=True)
    inscritos = models.ManyToManyField(Usuario, related_name='cursos_inscritos', blank=True)

    def __str__(self):
        return self.nombre