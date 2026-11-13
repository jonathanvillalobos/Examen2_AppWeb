# Comprensión Técnica - Portal de Servicios

## Actividad 1. Explicación integrada

Cuando el empleado abre su navegador web que actua como un **cliente** y escribe la dirección `http://127.0.0.1:5000/compra`, el navegador se conecta a la **dirección IP** local en el **puerto** 5000 usando el protocolo **HTTP** para enviar un **request** al **servidor**. En el **backend**, la aplicación desarrollada en **Python** con el framework **Flask** recibe la solicitud, ubica la **ruta** `/compra` y procesa un **template** que combina estructura **HTML** con diseño **CSS** y componentes de **Bootstrap**, El servidor devuelve esa vista en una **response** para dibujarla en el **frontend**. Despues, el empleado captura la cantidad y el precio en el formulario y lo envía mediante el método **POST**; La petición llega nuevamente a **Flask**, donde **Python** extrae los valores, hace los calculoss del subtotal, descuento y demas, y genera una nueva **response** renderizando el **template** con el **HTML** para mostrar el resultado en el **frontend**.

## Actividad 2. Diagrama explicado
flowchart LR
    A[Cliente: Navegador] -->|Petición POST| B[Servidor Flask 127.0.0.1:5000]
    B -->|Procesa y retorna HTML| C[Respuesta en pantalla]

    El cliente envía los datos mediante una petición POST hacia la IP:puerto (127.0.0.1:5000) donde escucha el servidor Flask. Ahí se realiza el procesamiento en Python y ocurre el retorno del HTML con el resultado hacia la pantalla.