import random
print("Adivinhe o número! (0-100)")
print("------------------------------")
num = random.randint(1,100)
tentativas = 0
historico = []


while True:
    palpite = input("Digite seu palpite: ")
    if not palpite.isdigit():
        print("Palpite inválido!")
        continue
   
    palpite = int(palpite) # passa p inteiro
    tentativas =+ 1
    historico.append(palpite)
   
    if palpite > num:
        print("Número errado! Palpite maior que número secreto.")
    elif palpite < num:
        print("Número errado! Palpite menor que número secreto.")
    elif palpite == num:
        print("Você acertou!")
        print(f"Seus palpites foram: {historico}")
        break
   