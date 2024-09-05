from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .simulation import ejecutar_simulacion
from .models import Resultado

class IniciarSimulacion(APIView):
    def post(self, request):
        simulacion = ejecutar_simulacion()
        return Response({"message": "Simulación iniciada", "simulacion_id": simulacion.id})

class VerResultados(APIView):
    def get(self, request, simulacion_id):
        resultados = Resultado.objects.filter(simulacion_id=simulacion_id)
        data = [{"gnomo": resultado.gnomo.nombre, "tarea": resultado.tarea, "exito": resultado.exito} for resultado in resultados]
        return Response(data)
