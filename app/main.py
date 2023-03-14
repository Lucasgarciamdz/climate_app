from flask import Flask, render_template

app = Flask(__name__, template_folder="/Users/LucasG/Desktop/itc_soluciones/climate_app/template")


@app.route("/")
def index():
    return render_template("index.html")
