A[Cliente: Navegador] -->|Petición POST| B[Servidor Flask 127.0.0.1:5000]
B -->|Procesamiento| C[Retorno de HTML]

El cliente envía los datos mediante una petición POST hacia la IP:puerto (127.0.0.1:5000) donde escucha el servidor Flask. Ahí se realiza el procesamiento en Python y ocurre el retorno del HTML con el resultado hacia la pantalla.


# Portal de Servicios

Aplicación web desarrollada con Python y Flask que reúne páginas informativas y
calculadoras para compras, salarios y conversión de temperaturas. La interfaz
utiliza plantillas Jinja2 y Bootstrap 5.2.

## Requisitos previos

- Python 3 instalado.
- `pip`, incluido con las versiones actuales de Python.

## Instalación

Clona o descarga el proyecto y abre una terminal en la carpeta raíz, donde se
encuentran `app.py` y `requirements.txt`.


Abre el portal en el navegador en <http://127.0.0.1:5000>.


