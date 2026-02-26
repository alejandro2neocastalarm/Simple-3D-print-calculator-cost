from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    coste = None
    venta = None
    if request.method == "POST":
        try:
            gramos = float(request.form.get("gramos", 0))
            precio_kg = float(request.form.get("precio", 0))
            margen = float(request.form.get("margen", 2))
            coste = round(gramos / 1000 * precio_kg * 4, 2)
            venta = round(coste * margen, 2)
        except ValueError:
            coste = "Error"
            venta = "Error"
    return render_template("index.html", coste=coste, venta=venta)

if __name__ == "__main__":
    app.run(debug=True)