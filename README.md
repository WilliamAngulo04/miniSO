# 🪟 miniSO - Mini Sistema Operativo Educativo

Aplicación gráfica educativa desarrollada en Python con Tkinter que simula componentes básicos de un sistema operativo, diseñada para facilitar el aprendizaje de conceptos fundamentales de sistemas operativos.

## 📋 Descripción

miniSO es una herramienta educativa interactiva que proporciona una interfaz gráfica intuitiva para explorar y comprender los componentes esenciales de un sistema operativo. A través de módulos independientes, los usuarios pueden interactuar con:

- **Explorador de Archivos**: Navegación visual del sistema de archivos
- **Gestión de Procesos**: Visualización y control de procesos en ejecución
- **Shell Educativa**: Terminal interactiva con comandos básicos
- **Información del Sistema**: Detalles sobre el hardware y software del equipo

## ✨ Características

- ✅ Interfaz gráfica moderna y amigable
- ✅ Módulos independientes y reutilizables
- ✅ Diseño basado en patrones de arquitectura de software
- ✅ Compatible con Windows y Linux (WSL)
- ✅ Navegación intuitiva con botones ilustrados
- ✅ Código modular y fácil de extender

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal
- **Tkinter**: Framework para la interfaz gráfica
- **Pillow (PIL)**: Procesamiento de imágenes
- **psutil**: Gestión de procesos del sistema

## 📦 Requisitos Previos

### En WSL/Linux:
```bash
sudo apt install python3-pip python3-venv python3-tk
```

### En Windows:
Python 3.x instalado desde [python.org](https://www.python.org/)

## 🚀 Instalación

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/WilliamAngulo04/miniSO
   cd miniSO
   ```

2. **Crea y activa un entorno virtual:**
   
   En Linux/WSL:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   En Windows:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecución

**En Windows:**
```powershell
python main.py
```
O doble clic en `main.py`

**En Linux/WSL:**
```bash
python3 main.py
```

## 📁 Estructura del Proyecto

```
miniSO/
├── main.py                 # Punto de entrada - Ventana principal
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Documentación
├── imgs/                  # Recursos visuales
│   ├── explorador.png     # Icono del explorador
│   ├── procesos.png       # Icono de procesos
│   ├── shell.png          # Icono de la shell
│   └── info.png           # Icono de información
├── styles/
│   └── styles.py          # Estilos y funciones de UI
└── scripts/               # Módulos funcionales
    ├── explorador.py      # Explorador de archivos
    ├── procesos.py        # Gestión de procesos
    ├── shell.py           # Terminal educativa
    └── info.py            # Información del sistema
```

## 🏗️ Arquitectura

El proyecto implementa una **arquitectura modular Hub-and-Spoke**:

- **Hub Central (`main.py`)**: Ventana principal que orquesta la navegación
- **Spokes (Módulos)**: Componentes independientes en `scripts/`
- **Separación de responsabilidades**: 
  - `styles/`: Presentación y diseño visual
  - `scripts/`: Lógica de negocio
  - `imgs/`: Recursos gráficos

### Patrones de Diseño:
- **Herencia**: Todos los módulos heredan de `tk.Toplevel`
- **Factory Pattern**: Funciones centralizadas para crear componentes UI
- **Callback Pattern**: Navegación entre módulos mediante callbacks

## 📚 Módulos Disponibles

### 1. 📁 Explorador de Archivos
- Navegación por directorios
- Listado de archivos y carpetas
- Funciones de subir nivel y refrescar

### 2. ⚙️ Gestión de Procesos
- Visualización de procesos activos (PID y nombre)
- Capacidad de finalizar procesos
- Actualización en tiempo real

### 3. 💻 Shell Educativa
- Comandos básicos: `ls`, `dir`, `pwd`, `echo`
- Terminal con estilo retro (fondo negro, texto verde)
- Historial de comandos ejecutados

### 4. 🧠 Información del Sistema
- Usuario actual
- Sistema operativo y versión
- Espacio en disco (total y libre)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request

## 👨‍💻 Autor

**William Angulo**
- GitHub: [@WilliamAngulo04](https://github.com/WilliamAngulo04)

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 🎓 Propósito Educativo

Este proyecto fue desarrollado como parte del curso de Sistemas Operativos con el objetivo de:
- Comprender la estructura básica de un sistema operativo
- Practicar programación orientada a objetos
- Implementar patrones de diseño de software
- Desarrollar interfaces gráficas de usuario
- Interactuar con recursos del sistema operativo
