import random


def gerar_tabuleiro(tamanho):
    grade = []
    for _ in range(tamanho):
        linha = ['~'] * tamanho
        grade.append(linha)
    return grade


def exibir_tabuleiro(grade):
    print("  ", end="")
    for i in range(len(grade)):
        print(i, end=" ")
    print()
    for i, linha in enumerate(grade):
        print(i, end=" ")
        for celula in linha:
            print(celula, end=" ")
        print()


def posicionar_embarcacoes(tamanho, total_navios):
    embarcacoes = []
    while len(embarcacoes) < total_navios:
        x = random.randint(0, tamanho - 1)
        y = random.randint(0, tamanho - 1)
        posicao = [x, y]
        if posicao not in embarcacoes:
            embarcacoes.append(posicao)
    return embarcacoes


def iniciar_batalha():
    dimensao = 5
    max_navios = 3
    embarcacoes = posicionar_embarcacoes(dimensao, max_navios)
    campo = gerar_tabuleiro(dimensao)
    navios_destruidos = 0


    print("Bem-vindo ao jogo Batalha Naval!")
    print(f"Tabuleiro de {dimensao}x{dimensao}. Há {max_navios} navios escondidos.")


    while navios_destruidos < max_navios:
        exibir_tabuleiro(campo)
        try:
            linha = int(input("Escolha a linha (0 a 4): "))
            coluna = int(input("Escolha a coluna (0 a 4): "))
        except:
            print("Entrada inválida. Digite números inteiros.")
            continue


        if linha < 0 or linha >= dimensao or coluna < 0 or coluna >= dimensao:
            print("Posição fora dos limites. Tente novamente.")
            continue


        if campo[linha][coluna] != '~':
            print("Você já atirou nessa posição. Tente outra.")
            continue


        if [linha, coluna] in embarcacoes:
            print("BOOM! Acertou um navio!")
            campo[linha][coluna] = 'X'
            navios_destruidos += 1
            print(f"Navios destruídos: {navios_destruidos} de {max_navios}")
        else:
            print("Splash! Só água.")
            campo[linha][coluna] = 'O'


    print("Parabéns! Você destruiu todos os navios inimigos!")
    exibir_tabuleiro(campo)


iniciar_batalha()
