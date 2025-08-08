# interfaz_grafica/panel_control.py

import customtkinter as ctk
from logica.proceso import Proceso

class PanelControl(ctk.CTkFrame):
    def __init__(self, master, gestor_memoria, planificador, panel_estado):
        super().__init__(master)
        self.gestor_memoria = gestor_memoria
        self.planificador = planificador
        self.panel_estado = panel_estado

        self.label_titulo = ctk.CTkLabel(self, text="Controles", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # Botón: Crear proceso
        self.boton_crear = ctk.CTkButton(self, text="Crear Proceso", command=self.crear_proceso)
        self.boton_crear.pack(pady=10)

        # Botón: Iniciar ejecución
        self.boton_iniciar = ctk.CTkButton(self, text="Iniciar", command=self.iniciar_planificador)
        self.boton_iniciar.pack(pady=10)

        # Botón: Detener ejecución
        self.boton_detener = ctk.CTkButton(self, text="Detener", command=self.detener_planificador)
        self.boton_detener.pack(pady=10)

        # Label informativo
        self.label_info = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.label_info.pack(pady=10)

    def crear_proceso(self):
        proceso = Proceso()
        agregado = self.planificador.agregar_proceso(proceso)

        if agregado:
            self.label_info.configure(text=f"✔️ Proceso '{proceso.nombre}' agregado.")
        else:
            self.label_info.configure(text=f"❌ No hay suficiente memoria para '{proceso.nombre}'.")

        self.panel_estado.actualizar_estado()

    def iniciar_planificador(self):
        self.planificador.iniciar()
        self.label_info.configure(text="▶️ Ejecución iniciada.")
        self.actualizar_estado_periodicamente()

    def detener_planificador(self):
        self.planificador.detener()
        self.label_info.configure(text="⛔ Ejecución detenida.")
        self.panel_estado.actualizar_estado()

    def actualizar_estado_periodicamente(self):
        self.panel_estado.actualizar_estado()
        if self.planificador.ejecutando:
            self.after(1000, self.actualizar_estado_periodicamente)
