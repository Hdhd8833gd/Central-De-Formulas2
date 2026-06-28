while True:
    print(f"Olá seja bem vindo a calculadora de formulas especificas\n"
          "aqui voce pode fazer calculos de fisica e algumas formulas matematicas")
    
    print("Escolha o tipo de fórmula")

    escolha = input("Matematica (M)\n"
                    "Física (F)\n").upper().strip()

    if escolha == "M":
        print("Operações de Matematica")

        aviso = (f"Escolha a operação\n"
         "Função Afim (1)\n etc (2)\n etc (3)\n")
        
        print(aviso)

        operacao = input("")
        
        match operacao:
            case "1":
                print("oi")

            case "2":
                print(12)

            case "3":
                print("olá")
        

    elif escolha == "F":
        print("Escolha a fórmula")

        recado = (f"Velocidade média (1)\nAceleração (2)\nAceleração (3)")
        print(recado)

        operacao_2 = input()

        match operacao_2:
            case "1":
                print("Velocidade média\n vm = Δs / Δt")

                deslocamento = float(input("Qual o deslocamento (espaço)? "))
                tempo = float(input("Qual o tempo (T)? "))

                unidade_tempo = input("Unidade do tempo (s / min / h): ").strip().lower()

                if unidade_tempo == "s":
                    tempo_segundos = tempo

                elif unidade_tempo == "min":
                    tempo_segundos = tempo * 60

                elif unidade_tempo == "h":
                    tempo_segundos = tempo * 3600

                else:
                    print("Unidade inválida")
                    break

                unidade = input("Escolha a unidade (m ou km): ").strip().lower()

                velocidade_media = deslocamento / tempo_segundos

                if unidade == "m":
                    print(f"Velocidade média: {velocidade_media} M/s")

                elif unidade == "km":
                    velocidade_kmh = velocidade_media * 3.6
                    print(f"Velocidade média: {velocidade_kmh} Km/h")

                else:
                    print("nenhum valor válido")

            case "2":
                print("Velocidade escalar\na = Δv / Δt\nvf - vi / tf - ti")

                velocidade_final = input("Digite a velocida final: ")
                velocidade_inicial = input("Digite a velocida inicial: ")
                tempo_final = input("Digite o tempo final: ")
                tempo_inicial = input("Digite o tempo inicial: ")

                calculo = velocidade_final - velocidade_inicial
                calculo2 = tempo_final - tempo_inicial
                resultado = calculo / calculo2

                print(resultado)


