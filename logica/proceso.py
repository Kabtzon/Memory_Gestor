# logica/proceso.py

import uuid
import random

import uuid
import random

class Proceso:
    def __init__(self, nombre=None, memoria_requerida=None, duracion=None):
        self.pid = self.generar_pid()
        pid_corto = str(self.pid)[-4:]
        self.nombre = nombre if nombre else f"P{pid_corto}"
        self.memoria_requerida = memoria_requerida if memoria_requerida else random.randint(10, 200)
        self.duracion = duracion if duracion else random.randint(1, 10)
        self.tiempo_restante = self.duracion
        self.estado = 'Listo'

    def generar_pid(self):
        return uuid.uuid4().int >> 64


    def ejecutar(self, tiempo=1):
        """Simula la ejecución del proceso reduciendo su tiempo restante"""
        if self.estado != 'Finalizado':
            self.tiempo_restante -= tiempo
            if self.tiempo_restante <= 0:
                self.tiempo_restante = 0
                self.estado = 'Finalizado'
            else:
                self.estado = 'Ejecutando'

    def finalizar(self):
        """Fuerza la finalización del proceso"""
        self.tiempo_restante = 0
        self.estado = 'Finalizado'

    def esta_terminado(self):
        return self.estado == 'Finalizado'

    def __str__(self):
        pid_corto = str(self.pid)[-4:]
        return (f"[{self.estado}] {self.nombre} (PID:{pid_corto}) | "
                f"RAM: {self.memoria_requerida} MB | "
                f"Duración: {self.duracion}s | Restante: {self.tiempo_restante}s")


