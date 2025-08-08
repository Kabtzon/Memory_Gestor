# logica/planificador.py

import threading
import time

class Planificador:
    def __init__(self, gestor_memoria):
        self.gestor_memoria = gestor_memoria
        self.procesos_en_espera = []         # Cola FIFO de espera
        self.procesos_en_ejecucion = {}      # pid: proceso
        self.bloqueo = threading.Lock()
        self.ejecutando = False

    def agregar_proceso(self, proceso):
        """Agrega un proceso: lo ejecuta si hay memoria, si no lo pone en espera"""
        with self.bloqueo:
            if self.gestor_memoria.reservar(proceso.pid, proceso.memoria_requerida):
                self._ejecutar_proceso(proceso)
                return True
            else:
                self.procesos_en_espera.append(proceso)
                return True  # También se considera agregado aunque esté en cola

    def iniciar(self):
        """Inicia el planificador principal"""
        if not self.ejecutando:
            self.ejecutando = True
            threading.Thread(target=self._monitor_procesos, daemon=True).start()

    def detener(self):
        """Detiene el planificador"""
        self.ejecutando = False

    def _monitor_procesos(self):
        """Hilo principal: intenta ejecutar procesos en espera cuando haya memoria"""
        while self.ejecutando:
            with self.bloqueo:
                disponibles = []
                for proceso in list(self.procesos_en_espera):  # Copia temporal
                    if self.gestor_memoria.reservar(proceso.pid, proceso.memoria_requerida):
                        self._ejecutar_proceso(proceso)
                        disponibles.append(proceso)

                # Remueve los que ya fueron iniciados
                for p in disponibles:
                    self.procesos_en_espera.remove(p)

            time.sleep(1)

    def _ejecutar_proceso(self, proceso):
        """Ejecuta un proceso en un hilo separado"""
        self.procesos_en_ejecucion[proceso.pid] = proceso
        proceso.estado = "Ejecutando"

        hilo = threading.Thread(target=self._ciclo_proceso, args=(proceso,), daemon=True)
        hilo.start()

    def _ciclo_proceso(self, proceso):
        """Simula el ciclo de vida de un proceso"""
        while proceso.tiempo_restante > 0 and self.ejecutando:
            proceso.ejecutar()
            time.sleep(1)

        # Al terminar
        proceso.finalizar()
        with self.bloqueo:
            self.gestor_memoria.liberar(proceso.pid)
            if proceso.pid in self.procesos_en_ejecucion:
                del self.procesos_en_ejecucion[proceso.pid]

    def obtener_procesos(self):
        """Devuelve procesos en espera"""
        return list(self.procesos_en_espera)

    def obtener_procesos_activos(self):
        """Devuelve procesos en ejecución"""
        return list(self.procesos_en_ejecucion.values())

    @property
    def proceso_actual(self):
        """Compatibilidad con interfaz anterior"""
        activos = self.obtener_procesos_activos()
        return activos[0] if activos else None
