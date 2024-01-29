from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contatos")
def contato():
    return render_template("contatos.html")

@app.route("/linguagens")
def linguagem():
    return render_template("linguagens.html")

@app.route("/projects")
def project():
    return render_template("projects.html")

@app.route("/projectPessoal")
def projects():
    return render_template("projectPessoal.html")

@app.route("/sobremim")
def sobre():
    return render_template("sobremim.html")

