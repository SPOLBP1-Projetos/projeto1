import random


def jogar_forca():
    lista_palavras = [
        "banana", "computador", "python", "brasil", "chuva", "janela", "amizade",
        "livro", "escola", "teclado", "monitor", "oceano", "bicicleta", "telefone",
        "historia", "energia", "programa", "rede", "estudo", "futebol"
    ]
    palavra_escolhida = random.choice(lista_palavras)
    letras_descobertas = []
    letras_tentadas = []
    erros_restantes = 6


    print("=== Jogo da Forca ===")


    while erros_restantes > 0:
        palavra_atual = ""
        for caractere in palavra_escolhida:
            if caractere in letras_descobertas:
                palavra_atual += caractere + " "
            else:
                palavra_atual += "_ "


        print("\nPalavra: " + palavra_atual.strip())
        print(f"Letras erradas: {', '.join(letras_tentadas)}")
        print(f"Tentativas restantes: {erros_restantes}")


        chute = input("Digite uma letra: ").lower()


        if len(chute) != 1 or not chute.isalpha():
            print("Digite só UMA letra válida.")
            continue


        if chute in letras_descobertas or chute in letras_tentadas:
            print("Você já tentou essa letra.")
            continue


        if chute in palavra_escolhida:
            print("Acertou!")
            letras_descobertas.append(chute)
        else:
            print("Errou!")
            letras_tentadas.append(chute)
            erros_restantes -= 1


        if all(letra in letras_descobertas for letra in palavra_escolhida):
            print(f"\nParabéns! Você adivinhou a palavra: {palavra_escolhida}")
            break


    if erros_restantes == 0:
        print(f"\nGame over! A palavra era: {palavra_escolhida}")


jogar_forca()
