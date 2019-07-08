from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route("/")
def index():
    jogo1 = Jogo('Super-Mario', 'Ação', 'Super Nintendo')
    jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
    lista = [jogo1, jogo2]
    return render_template("index.html", titulo='Jogos', 
                            jogos=lista)

app.run()