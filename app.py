from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="Inicio")


@app.route("/compra")
def compra():
    return render_template("compra.html", titulo="Compra")


@app.route("/salario")
def salario():
    return render_template("salario.html", titulo="Salario")


@app.route("/temperatura")
def temperatura():
    return render_template("temperatura.html", titulo="Temperatura")


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