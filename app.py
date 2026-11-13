import math

from flask import Flask, render_template, request

app = Flask(__name__)


def _leer_numero(nombre: str) -> float:
    etiqueta = nombre.replace("_", " ")
    try:
        valor = float(request.form[nombre])
    except (KeyError, ValueError) as error:
        raise ValueError(
            f"El campo {etiqueta} debe contener un número válido."
        ) from error

    if not math.isfinite(valor):
        raise ValueError(
            f"El campo {etiqueta} debe contener un número finito."
        )
    return valor


@app.route("/")
def index():
    return render_template("index.html", titulo="Inicio")


@app.route("/compra", methods=["GET", "POST"])
def compra():
    datos = {
        "titulo": "Compra",
        "cantidad": None,
        "precio_unitario": None,
        "subtotal": None,
        "descuento": None,
        "total": None,
        "resultado": None,
        "error": None,
    }

    if request.method == "POST":
        datos["cantidad"] = request.form.get("cantidad", "")
        datos["precio_unitario"] = request.form.get("precio_unitario", "")
        try:
            cantidad = _leer_numero("cantidad")
            precio_unitario = _leer_numero("precio_unitario")
            if cantidad < 0 or precio_unitario < 0:
                raise ValueError("La cantidad y el precio unitario no pueden ser negativos.")
        except ValueError as error:
            datos["error"] = str(error)
        else:
            subtotal = cantidad * precio_unitario
            descuento = subtotal * 0.10 if subtotal > 1000 else 0
            datos.update(
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                subtotal=subtotal,
                descuento=descuento,
                total=subtotal - descuento,
                resultado=True,
            )

    return render_template("compra.html", **datos)


@app.route("/salario", methods=["GET", "POST"])
def salario():
    datos = {
        "titulo": "Salario",
        "horas": None,
        "pago_hora": None,
        "horas_extra": None,
        "pago_normal": None,
        "pago_extra": None,
        "total_salario": None,
        "resultado": None,
        "error": None,
    }

    if request.method == "POST":
        datos["horas"] = request.form.get("horas", "")
        datos["pago_hora"] = request.form.get("pago_hora", "")
        try:
            horas = _leer_numero("horas")
            pago_hora = _leer_numero("pago_hora")
            if horas < 0 or pago_hora < 0:
                raise ValueError("Las horas y el pago por hora no pueden ser negativos.")
        except ValueError as error:
            datos["error"] = str(error)
        else:
            horas_extra = max(horas - 40, 0)
            pago_normal = min(horas, 40) * pago_hora
            pago_extra = horas_extra * pago_hora * 2
            datos.update(
                horas=horas,
                pago_hora=pago_hora,
                horas_extra=horas_extra,
                pago_normal=pago_normal,
                pago_extra=pago_extra,
                total_salario=pago_normal + pago_extra,
                resultado=True,
            )

    return render_template("salario.html", **datos)


@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    datos = {
        "titulo": "Temperatura",
        "celsius": None,
        "fahrenheit": None,
        "kelvin": None,
        "resultado": None,
        "error": None,
    }

    if request.method == "POST":
        datos["celsius"] = request.form.get("celsius", "")
        try:
            celsius = _leer_numero("celsius")
        except ValueError as error:
            datos["error"] = str(error)
        else:
            datos.update(
                celsius=celsius,
                fahrenheit=(celsius * 9 / 5) + 32,
                kelvin=celsius + 273.15,
                resultado=True,
            )

    return render_template("temperatura.html", **datos)


@app.route("/empresa")
def empresa():
    return render_template("empresa.html", titulo="Empresa")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html", titulo="Servicios")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html", titulo="Contacto")


if __name__ == "__main__":
    app.run(debug=True)