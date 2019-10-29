from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cursos.html')
def cursos():
    return render_template("cursos.html")


@app.route('/noticias.html')
def noticias():
    return render_template("noticias.html")


@app.route('/administracao.html')
def admin():
    return render_template("administracao.html")


@app.route('/engenhariadecomputacao.html')
def engenharia():
    return render_template("engenhariadecomputacao.html")


@app.route('/sistemasdeinformacao.html')
def sistemas():
    return render_template("sistemasdeinformacao.html")


@app.route('/cienciadacomputacao.html')
def ciencia():
    return render_template("cienciadacomputacao.html")


@app.route('/defesacibernetica.html')
def defesa():
    return render_template("defesacibernetica.html")


@app.route('/bancodedados.html')
def banco():
    return render_template("bancodedados.html")


@app.route('/jogosdigitais.html')
def jogos():
    return render_template("jogosdigitais.html")


@app.route('/redesdecomputadores.html')
def redes():
    return render_template("redesdecomputadores.html")


@app.route('/mecatronica.html')
def mecatronica():
    return render_template("mecatronica.html")


@app.route('/telecomunicacoes.html')
def telecomunicacoes():
    return render_template("telecomunicacoes.html")


app.run()
