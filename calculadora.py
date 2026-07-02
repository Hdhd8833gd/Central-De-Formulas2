from rich import print
from rich.panel import Panel

while True:
    print(Panel("[cyan]\nOlá seja bem vindo a calculadora de formulas especificas[/cyan]\n"))
    
    print("[yellow]Escolha o tipo de fórmula[/yellow]")

    escolha = input("Matematica (M)\nFísica (F)\n").upper().strip()

    if escolha == "M" or escolha == "MATEMATICA":
        print(Panel("[cyan]Operações de Matematica[/cyan]"))

        aviso = (f"Escolha a operação\n"
         "Funções (1)\nEstudo do sinal da função (2)\netc (3)\n")
        
        print(aviso)

        operacao = input("")
        
        match operacao:
            case "1":
                print("[green]Funções\nF(X)= A . X + B[/green]")

                valor_a = float(input("Digite o valor de A: "))
                valor_b = float(input("Digite o valor de B: "))
                valor_x = float(input("Digite o valor de X (Variável): "))
                
                calculo_funcao = valor_a * valor_x + valor_b
                resultado_afim = calculo_funcao

                if valor_a == 0 and valor_b == 0:
                    print(f"A função é [green]identidade[/green]\no resultado será o mesmo valor de X então Y = {valor_x}")

                else:
                    print(f"Para o valor de X ({valor_x}) Y é: {resultado_afim}")


            case "2":
                print("Estudo do sinal da função\n-B/A")

                estudo_b = float(input("Digite o valor de B: "))
                estudo_a = float(input("Digite o valor de A: "))
        

                if estudo_a > 0:
                 calculo_estudo = -estudo_b / estudo_a
                 resultado_estudo = calculo_estudo
                 print(f"A função é [green]positiva[/green]\nF positivo se X > {resultado_estudo}\nF negativo se X < {resultado_estudo}")

                elif estudo_a < 0:
                  calculo_estudo = -estudo_b / estudo_a
                  resultado_estudo = calculo_estudo
                  print(f"A função é [yellow]negativa[/yellow]\nF positivo se X < {resultado_estudo}\nF negativo se X > {resultado_estudo}")


                elif estudo_a == 0:
                    print(f"A função é [green]constante[/green]\no valor será sempre o valor de B {estudo_b}\no valor do eixo Y nunca mudará")

                else:
                    print("[red]ERRO nenhum valor válido[/red]")
                    continue


            case "3":
                print("olá")
        

    elif escolha == "F" or escolha == "FISICA":
        print(Panel("[cyan]Fórmulas de física[/cyan]"))

        recado = ("Velocidade média (1)\nAceleração (2)\nAceleração (3)")
        print(recado)

        operacao_2 = input()

        match operacao_2:
            case "1":
                print("[green]Velocidade média\n vm = Δs / Δt[/green]")

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
                    print("[red]Unidade inválida[/red]")
                    continue

                unidade = input("Escolha a unidade (m ou km): ").strip().lower()

                velocidade_media = deslocamento / tempo_segundos

                if unidade == "m":
                    print(Panel(f"[blue]Velocidade média: {velocidade_media} M/s[/blue]"))

                elif unidade == "km":
                    velocidade_kmh = velocidade_media * 3.6
                    print(Panel(f"[blue]Velocidade média: {velocidade_kmh} Km/h[/blue]"))

                else:
                    print("[red]nenhum valor válido[/red]")

            case "2":
                print("[green]Aceleração\na = Δv / Δt\nvf - vi / tf - ti[/green]")

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
                   temp_ms =  tempo_final * 60
                   temp_msi = tempo_inicial * 60
                   print("M/s")

                elif unidade_medida_temp == "H":
                    temp_ms = tempo_final * 3600
                    temp_msi = tempo_inicial * 3600

                else:
                    print("[red]nenhum valor válido[/red]")
                    continue

                unidade_velocidade = input("Qual a unidade de medida da velocidade:\n" \
                "m/s km/h\n").lower().strip()

                if unidade_velocidade == "m/s":
                    velo_padrao1 = velocidade_final
                    velo_padrao2 = velocidade_inicial

                elif unidade_velocidade == "km/h":
                    velo_padrao1 = velocidade_final / 3.6
                    velo_padrao2 = velocidade_inicial / 3.6

                else:
                    print("[red]ERRO nenhum valor válido[/red]")
                    continue

                calculo = velo_padrao1 - velo_padrao2
                calculo2 = temp_ms - temp_msi
                resultado = calculo / calculo2

                print(Panel(f"[blue]Resultado = {resultado}m/s²[/blue]"))


