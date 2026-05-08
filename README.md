# ProyectoSENA

Proyecto Flask + PostgreSQL para abrir en Visual Studio Code.

## Requisitos
- Python 3.10+
- PostgreSQL con base de datos `gestion` (usuario `postgres`, contraseña `123456`)
- VS Code con la extensión de Python

## Instalación
Abre la carpeta `ProyectoSENA` en VS Code y en la terminal ejecuta:

```bash
pip install Flask psycopg2-binary
```

## Probar conexión a PostgreSQL
```bash
python config.py
```
Debe imprimir: `Conexión a PostgreSQL establecida correctamente`.

## Ejecutar la aplicación
```bash
python app.py
```
Abre en el navegador: http://127.0.0.1:5000/ProyectoSENA
(La raíz `/` redirige automáticamente al index.)

## Estructura
```
ProyectoSENA/
├── app.py
├── config.py
├── static/
│   ├── estilos.css
│   └── fondo.jpg
└── templates/
    ├── bootstrap.html
    ├── menu.html
    └── index.html
```
