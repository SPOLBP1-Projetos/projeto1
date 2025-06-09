def iniciar_quiz():
    #lista armazenando um dicionario pra ser mais facil acessar pr indices
    questoes = [
        {
            "enunciado": "1. Qual é o planeta mais próximo do Sol?",
            "alternativas": ["A) Vênus", "B) Terra", "C) Mercúrio", "D) Marte"],
            "correta": "C"
        },
        {
            "enunciado": "2. Qual é o nome da estrela mais próxima da Terra, além do Sol?",
            "alternativas": ["A) Betelgeuse", "B) Alfa Centauri", "C) Sirius", "D) Proxima Centauri"],
            "correta": "D"
        },
        {
            "enunciado": "3. Qual o resultado da conversão do número binário 010110?",
            "alternativas": ["A) 22", "B) 32", "C) 21", "D) 20"],
            "correta": "A"
        },
        {
            "enunciado": "4. Qual é o maior satélite natural do planeta Saturno?",
            "alternativas": ["A) Io", "B) Europa", "C) Lua", "D) Titã"],
            "correta": "D"
        },
        {
            "enunciado": "5. O que é uma supernova?",
            "alternativas": ["A) O brilho de um cometa ao se aproximar do Sol", "B) Formação de uma nova estrela", "C) Explosão de uma estrela massiva no final de sua vida", "D) Colisão entre dois planetas"],
            "correta": "C"
        }
    ]

    while True:
        pontos = 0
        for questao in questoes: #Cria automaticamente a variavel questao e itera com o dicionario "questoes"
            print("\n") #Pula de linha a cada questao e alternativa
            print(questao["enunciado"]) #Exibe o enunciado que é uma chave "enunciado"

        
            for alternativa in questao["alternativas"]:
                print(alternativa) # exibe as alternativas

        print("\n")
        resposta = input("Sua resposta: ").strip().upper() #remove os espaços e transforma sua resposta em maiusculo 

        if resposta == questao["correta"].upper():
            print("Resposta correta! :D")
            pontos += 1 #soma a pontuação
        else:
            print(f"Resposta incorreta! :( A resposta era: Letra {questao["correta"]}")




iniciar_quiz()

