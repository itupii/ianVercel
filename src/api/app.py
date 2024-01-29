from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/templates/index.html')

@app.route('/projects')
def projects():
    return render_template('/templates/projects.html')

@app.route('/projectPessoal')
def projectPessoal():
    return render_template('/templates/projectPessoal.html')

@app.route('/sobremim')
def sobremim():
    return render_template('/templates/sobremim.html')

@app.route('/linguagens')
def linguagens():
    return render_template('/templates/linguagens.html')

@app.route('/contatos')
def contatos():
    return render_template('/templates/contatos.html')


if __name__ == '__main__':
    app.run(debug=True)