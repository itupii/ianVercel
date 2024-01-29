from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/linguagens")
def linguagens():
    return render_template("linguagens.html")

@app.route("/projects")
def projects():
    return render_template("templates/projects.html")

@app.route("/projectPessoal")
def projectPessoal():
    return render_template("projectPessoal.html")

@app.route("/sobremim")
def sobremim():
    return render_template("sobremim.html")

if __name__ == "__main__":
    app.run(debug=True)