from django.db import models

# Create your models here.

class Gnomo(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    habilidad = models.FloatField()  # Valor entre 0.0 y 1.0

    def __str__(self):
        return f"{self.nombre} - {self.rol}"

class Simulacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)

class Resultado(models.Model):
    gnomo = models.ForeignKey(Gnomo, on_delete=models.CASCADE)
    simulacion = models.ForeignKey(Simulacion, on_delete=models.CASCADE)
    tarea = models.CharField(max_length=100)
    exito = models.BooleanField()

    def __str__(self):
        return f"Resultado de {self.gnomo} en {self.tarea}: {'Éxito' si exito else 'Fallo'}"

