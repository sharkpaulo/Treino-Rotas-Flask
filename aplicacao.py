from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cursos.html')
def cursos():
    return render_template("cursos.html")


@app.route('/')
def noticias():
    return render_template("noticias.html")


@app.route('/')
def admin():
    return render_template("administracao.html")


@app.route('/')
def engenharia():
    return render_template("engenhariadecomputacao.html")


@app.route('/')
def sistemas():
    return render_template("sistemasdeinformacao.html")


@app.route('/')
def ciencia():
    return render_template("cienciadacomputacao.html")


@app.route('/')
def defesa():
    return render_template("defesacibernetica.html")


@app.route('/')
def banco():
    return render_template("bancodedados.html")


@app.route('/')
def jogos():
    return render_template("jogosdigitais.html")


@app.route('/')
def redes():
    return render_template("redesdecomputadores.html")


@app.route('/')
def mecatronica():
    return render_template("mecatronica.html")


@app.route('/')
def telecomunicacoes():
    return render_template("telecomunicacoes.html")


app.run()
