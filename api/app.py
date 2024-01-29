from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("/public/index.html")

@app.route("/contatos")
def contatos():
    return render_template("/public/contatos.html")

@app.route("/linguagens")
def linguagens():
    return render_template("/public/linguagens.html")

@app.route("/projects")
def projects():
    return render_template("/public/projects.html")

@app.route("/projectPessoal")
def projectPessoal():
    return render_template("/public/projectPessoal.html")

@app.route("/sobremim")
def sobremim():
    return render_template("/public/sobremim.html")

if __name__ == "__main__":
    app.run(debug=True)