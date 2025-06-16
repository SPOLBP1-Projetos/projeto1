def exibir_hastes(hastes):
    print("\nEstado atual das hastes:")
    for idx, haste in enumerate(hastes):
        print(f"Haste {idx + 1}: {haste}")
    print()


def movimento_valido(hastes, de_onde, para_onde):
    if not hastes[de_onde]:
        return False
    if not hastes[para_onde]:
        return True
    return hastes[de_onde][-1] < hastes[para_onde][-1]


def transferir_disco(hastes, de_onde, para_onde):
    disco = hastes[de_onde].pop()
    hastes[para_onde].append(disco)


def jogo_hanoi():
    total_discos = 3
    while True:
        try:
            total_discos = int(input("Quantos discos? (3 a 5): "))
            if 3 <= total_discos <= 5:
                break
            else:
                print("Escolha entre 3 e 5 discos.")
        except:
            print("Digite um número válido.")


    hastes = [list(range(total_discos, 0, -1)), [], []]


    print("Objetivo: mover todos os discos da haste 1 para a haste 3.")
    exibir_hastes(hastes)


    while len(hastes[2]) != total_discos:
        try:
            origem = int(input("Mover disco de qual haste? (1, 2 ou 3): ")) - 1
            destino = int(input("Para qual haste? (1, 2 ou 3): ")) - 1
        except:
            print("Digite um número válido.")
            continue


        if origem not in [0, 1, 2] or destino not in [0, 1, 2]:
            print("Escolha hastes entre 1 e 3.")
            continue


        if not movimento_valido(hastes, origem, destino):
            print("Movimento inválido! Tente novamente.")
            continue


        transferir_disco(hastes, origem, destino)
        exibir_hastes(hastes)


    print("Parabéns! Você resolveu a Torre de Hanói!")


jogo_hanoi()
