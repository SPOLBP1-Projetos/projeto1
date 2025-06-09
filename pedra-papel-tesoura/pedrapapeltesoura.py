import random


def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    vencer = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }


    while True:
        sua_escolha = input("Escolha pedra, papel ou tesoura: ").strip().lower() # .strip() tira os espaços quando vc digita algo e .lower() deixa o que voce digitou tudo minusculo pra facilitar a comparação.
        if sua_escolha not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue


        escolha_pc = random.choice(opcoes)
        print(f"Você escolheu: {sua_escolha}")
        print(f"Computador escolheu: {escolha_pc}")


        if sua_escolha == escolha_pc:
            print("Empate!")
        elif vencer[sua_escolha] == escolha_pc:
        # ao fazer variavel[outra_variavel], estariamos acessando algo dentro da estrutura usando o valor da segunda variável. Neste caso, como a variavel "vencer" é um dicionário que armazena quem ganha de quem, pegando a variavel que armazena o dicionario (no caso, é "vencer") e pegar "sua_escolha" estariamos fazendo o seguinte:
        # se sua_escolha == papel e escolha_pc == pedra
        # volta pro dicionario, acha que 'papel: pedra' (ganha de pedra) e exibe "Você venceu!"
            print("Você venceu!")
        else:
            # se caso sua_escolha == tesoura e escolha_pc == pedra
            # volta pro dicionario onde 'pedra:tesoura' (pedra ganha de tesoura) e exibe "Você perdeu!"
            print("Você perdeu!")
            # Sendo assim, você acessará uma variável com um dicionario por exemplo, usando outra variável de índice pra acesso.


        jogar_novamente = input("Jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Jogo finalizado.")
            break


jogar() # chama a funcao def jogar()
