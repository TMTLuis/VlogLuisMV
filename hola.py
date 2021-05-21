from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/template")
def url_principal():
	return render_template("template.html", nombre="Luis Morales Vazquez", edad="24 años", lugar="Guanajuato");

@app.route("/hobbies")
def hobbies():
	return render_template("hobbies.html", nombre="Luis Morales Vazquez");

@app.route("/lugares")
def lugares():
	return render_template("lugares.html", nombre="Luis Morales Vazquez");

@app.route("/mascotas")
def mascotas():
	return render_template("mascotas.html", nombre="Luis Morales Vazquez");

if __name__ == "__main__":
	app.run(debug=True)


