from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

#  JOGO 1: Adivinhe o número 
numero_secreto = random.randint(0, 100)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/numero", methods=["GET", "POST"])
def numero():
    global numero_secreto
    mensagem = ""
    if request.method == "POST":
        palpite = int(request.form["palpite"])
        if palpite == numero_secreto:
            mensagem = "🎉 Você acertou!"
            numero_secreto = random.randint(0, 100)
        elif palpite < numero_secreto:
            mensagem = "O número é maior!"
        else:
            mensagem = "O número é menor!"
    return render_template("numero.html", mensagem=mensagem)

#  JOGO 2: Batalha Naval
tabuleiro = [["~"]*5 for _ in range(5)]
navio = (random.randint(0,4), random.randint(0,4))

@app.route("/batalha", methods=["GET","POST"])
def batalha():
    mensagem = ""
    if request.method == "POST":
        x = int(request.form["x"])
        y = int(request.form["y"])
        if (x,y) == navio:
            mensagem = "🚢 Você acertou o navio!"
        else:
            mensagem = "💦 Água!"
    return render_template("batalha.html", mensagem=mensagem)

#  JOGO 3: Forca
palavra = "python"
estado = ["_"]*len(palavra)

@app.route("/forca", methods=["GET","POST"])
def forca():
    global estado
    mensagem = ""
    if request.method == "POST":
        letra = request.form["letra"].lower()
        if letra in palavra:
            for i,c in enumerate(palavra):
                if c == letra:
                    estado[i] = letra
        else:
            mensagem = "❌ Letra errada!"
        if "_" not in estado:
            mensagem = "🎉 Você venceu!"
            estado = ["_"]*len(palavra)
    return render_template("forca.html", estado=" ".join(estado), mensagem=mensagem)

# JOGO 4: Pedra/Papel/Tesoura 
@app.route("/rps", methods=["GET","POST"])
def rps():
    mensagem = ""
    if request.method == "POST":
        escolha = request.form["escolha"]
        opcoes = ["Pedra","Papel","Tesoura"]
        computador = random.choice(opcoes)
        if escolha == computador:
            mensagem = f"Empate! Ambos escolheram {escolha}"
        elif (escolha=="Pedra" and computador=="Tesoura") or \
             (escolha=="Papel" and computador=="Pedra") or \
             (escolha=="Tesoura" and computador=="Papel"):
            mensagem = f"🎉 Você ganhou! Computador escolheu {computador}"
        else:
            mensagem = f"😢 Você perdeu! Computador escolheu {computador}"
    return render_template("rps.html", mensagem=mensagem)

# JOGO 5: Quiz 
@app.route("/quiz", methods=["GET","POST"])
def quiz():
    perguntas = [
        {
            "pergunta": "Qual linguagem estamos usando?",
            "alternativas": ["Python", "Java", "C++"],
            "correta": "Python"
        },
        {
            "pergunta": "Qual o sentido da vida?",
            "alternativas": ["Comer", "Viver", "Deus"],
            "correta": "Deus"
        },
        {
            "pergunta": "Quanto é 2 + 2? (pegadinha insana)",
            "alternativas": ["3", "4", "5"],
            "correta": "4"
        },
        {
            "pergunta": "Quantos anos Jesus Cristo viveu no seu período mortal?",
            "alternativas": ["31", "32", "33"],
            "correta": "33"
        }
    ]

    #sorteia uma pergunta
    pergunta_atual = random.choice(perguntas)
    mensagem = ""

    if request.method == "POST":
        resposta = request.form["resposta"]
        correta = request.form["correta"]
        if resposta == correta:
            mensagem = "🎉 Correto!"
        else:
            mensagem = f"❌ Errado! A resposta correta era {correta}."

    return render_template(
        "quiz.html",
        pergunta=pergunta_atual["pergunta"],
        alternativas=pergunta_atual["alternativas"],
        correta=pergunta_atual["correta"],
        mensagem=mensagem
    )

#  JOGO 6: Torre de Hanoi (rever esse codigo)
def hanoi_solver(n, origem, destino, auxiliar, movimentos):
    if n == 1:
        movimentos.append(f"Mova disco 1 de {origem} para {destino}")
        return
    hanoi_solver(n-1, origem, auxiliar, destino, movimentos)
    movimentos.append(f"Mova disco {n} de {origem} para {destino}")
    hanoi_solver(n-1, auxiliar, destino, origem, movimentos)

@app.route("/hanoi", methods=["GET","POST"])
def hanoi():
    movimentos = []
    if request.method == "POST":
        discos = int(request.form["discos"])
        hanoi_solver(discos, "A", "C", "B", movimentos)
    return render_template("hanoi.html", movimentos=movimentos)


if __name__ == "__main__":
    app.run(debug=True, port=(5002))
