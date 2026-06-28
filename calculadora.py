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
                print("Aceleração\na = Δv / Δt\nvf - vi / tf - ti")

                velocidade_final = float(input("Digite a velocida final: "))
                velocidade_inicial = float(input("Digite a velocida inicial: "))
                tempo_final = float(input("Digite o tempo final: "))
                tempo_inicial = float(input("Digite o tempo inicial: "))
                unidade_medida_temp = input("Qual a unidade de medida do tempo:\ns m h\n").upper().strip()

                if unidade_medida_temp == "S":
                    temp_ms = tempo_final
                    temp_msi = tempo_inicial
                    print("km/h")

                elif unidade_medida_temp == "M":
                   temp_ms =  tempo_final / 60
                   temp_msi = tempo_inicial / 60
                   print("M/s")

                elif unidade_medida_temp == "H":
                    temp_ms / 3600
                    temp_msi / 3600

                else:
                    print("nenhum valor válido")

                unidade_velocidade = input("Qual a unidade de medida da velocidade:\n" \
                "m/s km/h\n").lower().strip()

                if unidade_velocidade == "m/s":
                    velo_padrao1 = velocidade_final
                    velo_padrao2 = velocidade_inicial

                elif unidade_velocidade == "km/h":
                    velo_padrao1 = velocidade_final / 3.6
                    velo_padrao2 = velocidade_inicial / 3.6

                calculo = velo_padrao1 - velo_padrao2
                calculo2 = temp_ms - temp_msi
                resultado = calculo / calculo2

                print(f"{resultado}m/s²")


