from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Gnomo(models.Model):
    ROLES = [
        ('PANADERO', 'Panadero'),
        ('CHEF_SOPAS', 'Chef de sopas'),
        ('PASTELERO', 'Pastelero'),
        ('CARNICERO', 'Carnicero'),
        ('APRENDIZ', 'Aprendiz'),
    ]

    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES)
    habilidad = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])  # Valor entre 0.0 y 1.0 asegurado

    def __str__(self):
        return f"{self.nombre} - {self.get_rol_display()}" # get_rol_display() es para obtener el valor del choice

class Simulacion(models.Model):
    # Sugerencia! - En caso de querer llevar una simulación detallada puedes llevar a hacer un fecha fin/fecha inicio. 
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Simulación del {self.fecha.strftime('%d/%m/%Y %H:%M')}"

class Resultado(models.Model):
    gnomo = models.ForeignKey(Gnomo, on_delete=models.CASCADE, related_name='resultados') #Related name es para acceder a los resultados de un gnomo
    simulacion = models.ForeignKey(Simulacion, on_delete=models.CASCADE, related_name='resultados')
    tarea = models.CharField(max_length=100)
    exito = models.BooleanField()

    def __str__(self):
        return f"Resultado de {self.gnomo} en {self.tarea}: {'Éxito' if self.exito else 'Fallo'}"