#  Memory_Gestor

Simulador de gestión de procesos con control de memoria RAM, desarrollado como proyecto de semestre. El sistema muestra en tiempo real el comportamiento de un sistema operativo al manejar múltiples procesos que compiten por espacio en memoria. Incluye una interfaz gráfica moderna, paneles de control e indicadores visuales similares al Administrador de Tareas de Windows.

---

##  Características

- Simulación realista de ejecución de procesos.
- Límite de memoria RAM configurable (por defecto: 1024 MB).
- Cola de espera para procesos sin memoria disponible.
- Ejecución concurrente de múltiples procesos usando hilos (`threading`).
- Visualización gráfica del uso de memoria en tiempo real.
- Barra de progreso, lista de procesos activos y en espera.
- Interfaz moderna con `customtkinter`.

---

##  Estructura del proyecto

```
Memory_Gestor/
│
├── logica/
│   ├── proceso.py              # Modelo de procesos
│   ├── planificador.py         # Planificación y ejecución
│   └── gestor_memoria.py       # Administración de memoria
│
├── interfaz_grafica/
│   ├── ventana_principal.py    # Ventana principal
│   ├── panel_control.py        # Botones: crear, iniciar, detener
│   └── panel_estado.py         # Barra, procesos y gráfica
│
├── main.py                     # Punto de entrada
├── requirements.txt            # Dependencias necesarias
└── README.md                   # Este archivo
```

---

##  Configuración YAML de ejemplo

A continuación se muestra un archivo `config.yml` usado para definir la configuración del simulador:

```yaml
nombre: Memory_Gestor
version: 1.0
autor: Grupo de Trabajo
memoria:
  total: 1024
  alerta_rojo: 80
  alerta_naranja: 60
interfaz:
  modo: oscuro
  idioma: es
```

---

##  Instalación y ejecución en Windows

>  **Versión recomendada de Python: [3.13](https://www.python.org/downloads/release/python-3130/)**  
> Asegúrate de marcar **"Add Python to PATH"** al instalarlo.

###  Pasos para ejecutar el simulador

#### 1. Clona el repositorio

```bash
git clone https://github.com/Kabtzon/Memory_Gestor.git
cd Memory_Gestor
```

#### 2. Configura la ejecución de scripts (PowerShell)

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

#### 3. Crea un entorno virtual con Python 3.13

```bash
py -3.13 -m venv venv
```

#### 4. Activa el entorno virtual

```bash
venv\Scripts\activate
```

#### 5. Instala las dependencias

```bash
pip install -r requirements.txt
```

#### 6. Ejecuta el simulador

```bash
python main.py
```

#### 7. Desactiva el entorno virtual

```bash
deactivate
```

---

##  Tecnologías utilizadas

- Python 3.13
- `customtkinter`
- `matplotlib`
- `threading`
- `tkinter`
- `numpy`

---

##  Comportamiento del simulador

- Cada proceso consume entre **10 MB y 200 MB**.
- La duración de los procesos es entre **1 y 10 segundos**.
- Si no hay memoria suficiente, el proceso entra en **cola de espera**.
- La ejecución se realiza en **tiempo real**.
- El gráfico del uso de memoria cambia de color dinámicamente:
  - 🟢 Verde: < 60%
  - 🟠 Naranja: 60–80%
  - 🔴 Rojo: > 80%
 
  - <img width="1014" height="611" alt="image" src="https://github.com/user-attachments/assets/6d6cf4f1-f63c-4200-a618-9b529b4ff419" />
  - <img width="1006" height="620" alt="image" src="https://github.com/user-attachments/assets/5136497a-b384-4754-9253-0a9d96a39b69" />
  - <img width="1007" height="608" alt="image" src="https://github.com/user-attachments/assets/f843ae33-26ae-4cb5-b256-9b16be8e27e8" />




---

##  Autoría

Este proyecto fue desarrollado por el **Grupo de Trabajo** como parte del curso de Sistemas Operativos.

---

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Puedes reutilizarlo y modificarlo libremente con fines académicos o personales.
