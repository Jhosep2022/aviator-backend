# Aviator

Aviator es una aplicación web construida con FastAPI para el backend y React para el frontend. Esta guía te llevará a través del proceso de configuración y puesta en marcha del proyecto.

## Requisitos Previos

- Python 3.6+
- Node.js y npm
- MySQL

## Configuración del Backend

### 1. Clonar el repositorio

```sh
git clone <URL_DEL_REPOSITORIO>
cd aviator/backend
```

2. Crear y activar un entorno virtual
python -m venv venv
.\venv\Scripts\activate  # En Windows
source venv/bin/activate  # En macOS/Linux

3. Instalar las dependencias
```sh
pip install 
```

4. Inicializar la base de datos
Asegúrate de tener una base de datos MySQL creada. Los modelos se crearán automáticamente al iniciar el servidor.

5. Ejecutar el servidor
```sh
Copiar código
uvicorn app.main:app --reload
```
