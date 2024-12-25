from flask import Flask, request

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>Home</h1>"

@app.route("/")
def pocetna_strana():
    return "<h1>Pocetna strana</h1>"

@app.route("/pozdrav", defaults = {"name": "Ivana"})
@app.route("/pozdrav/<name>")
def pozdrav(name):
    return f"<h1>Pozdrav do {name} </h1>"

@app.route("/kvadrat",defaults={"broj": ""})
@app.route("/kvadrat")
def kvadrat():
    broj = request.args.get("broj")
    try:
        k = int(broj) * int(broj)
        return f"<h1> {k} </h1>"
    except ValueError:
        return f"<h1>Vnesete broj vo url </h1>"


@app.route("/sobiranje", defaults={"a": "", "b": ""})
@app.route("/sobiranje/<a>/<b>")
def sobiranje(a,b):
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        zbir = int(a) + int(b)
        return f"<h1>Zbirot e {zbir} </h1>"
    except ValueError:
        return "<h1>Vnesete validni broevi vo URL </h1>"


@app.route("/name")
def name():
    ime = request.args.get("ime")
    prezime = request.args.get("prezime")
    return f"<h1> Moeto ime e {ime} {prezime} <h1>"

if __name__ == "__main__":
    app.run(debug=True)