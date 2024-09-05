import random
from .models import Gnomo, Simulacion, Resultado

def simular_tarea(habilidad):
    """Simula una tarea basada en la habilidad del gnomo."""
    probabilidad = random.uniform(0, 1)
    return probabilidad <= habilidad

def ejecutar_simulacion():
    """Ejecuta la simulación para todos los gnomos y guarda los resultados."""
    simulacion = Simulacion.objects.create()
    resultados = []
    
    for gnomo in Gnomo.objects.all():
        tarea = f"Preparar {gnomo.rol}"
        exito = simular_tarea(gnomo.habilidad)
        resultados.append(Resultado(gnomo=gnomo, simulacion=simulacion, tarea=tarea, exito=exito))
    
    # Guardar todos los resultados en la base de datos
    Resultado.objects.bulk_create(resultados)
    return simulacion
