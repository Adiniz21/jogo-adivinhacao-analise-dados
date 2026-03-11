import os
import random
import json
from datetime import datetime

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogar():
    while True:
        print("Você escolheu a opção de jogar")
        print("Para iniciar o jogo, escolha a dificuldade que você irá querer")
        print("1- Para a dificuldade fácil, tendo o intervalo de 1 a 50")
        print("2- Para a dificuldade médio, tendo o intervalo de 1 a 100")
        print("3- Para a dificuldade dificil, tendo o intervalo de 1 a 500")
        print("4- Sair")

        try:
            escolha = int(input("Escolha uma opção: "))            
        except ValueError:
            print("Escolha uma opção válida!")
            input("Pressione ENTER para continuar...")
            continue

        limpar_tela()

        match escolha: 
            case 1:
                limpar_tela()
                print("Você escolheu a opção fácil")
                numero_sorteado = random.randint(1,50)
                
                while True:
                    nome_usuario = input("Para iniciar insira o seu nome por favor: ")

                    if len(nome_usuario) == 0:
                        print("Nome do usuário não pode ser vazio")
                    else:
                        break
                
                contador = 0
                print("Agora o jogo está iniciando")
                while True:
                    contador +=1
                    try:
                        numero_escolido = int(input("Escolha uma opção: "))
                        data_atual = datetime.now()
                        data_formatada = data_atual.strftime("%d/%m/%y %H:%M:%S")
                        if numero_sorteado == numero_escolido:
                            print(f"Parabéns você acertou {nome_usuario}, você acertou o número sorteado que foi, {numero_sorteado} com {contador} tentativas") 
                            arquivo = os.path.join("projeto", "ranking.json")

                            if not os.path.exists(arquivo):
                                with open(arquivo, "w", encoding="utf-8") as f:
                                    json.dump([], f, indent=4, ensure_ascii=False)

                            with open(arquivo, "r", encoding="utf-8") as f:
                                ranking = json.load(f)

                            ranking.append({
                                "nome": nome_usuario,
                                "tentativas": contador,
                                "numero_sorteado": numero_sorteado,
                                "dificuldade": "Fácil",
                                "data": data_formatada
                            })

                            with open(arquivo, "w", encoding="utf-8") as f:
                                json.dump(ranking, f, indent=4, ensure_ascii=False)

                            input("Pressione ENTER para continuar...") 
                            return         
                        else:
                            print("Você ainda não acertou o número, tente novamente")
                            print("tentativas: ", contador)
                            if numero_escolido > numero_sorteado:
                                print("O número escolhido é maior.")
                                input("Pressione ENTER para continuar...")
                            else:
                                print("O número escolhido é menor")
                                input("Pressione ENTER para continuar...")
                            limpar_tela()
                    except ValueError:
                        print("Escolha uma opção válida!")
                        input("Pressione ENTER para continuar...")
                        continue

                
            case 2: 
                limpar_tela()
                print("Você escolheu a opção Médio")
                numero_sorteado = random.randint(1,100)
                while True:
                    nome_usuario = input("Para iniciar insira o seu nome por favor: ")

                    if len(nome_usuario) == 0:
                        print("Nome do usuário não pode ser vazio")
                    else:
                        break
                
                contador = 0
                print("Agora o jogo está iniciando")
                while True:
                    contador +=1
                    try:
                        numero_escolido = int(input("Escolha uma opção: "))
                        data_atual = datetime.now()
                        data_formatada = data_atual.strftime("%d/%m/%y %H:%M:%S")
                        if numero_sorteado == numero_escolido:
                            print(f"Parabéns você acertou {nome_usuario}, você acertou o número sorteado que foi, {numero_sorteado} com {contador} tentativas") 
                            arquivo = os.path.join("projeto", "ranking.json")

                            if not os.path.exists(arquivo):
                                with open(arquivo, "w", encoding="utf-8") as f:
                                    json.dump([], f, indent=4, ensure_ascii=False)

                            with open(arquivo, "r", encoding="utf-8") as f:
                                ranking = json.load(f)

                            ranking.append({
                                "nome": nome_usuario,
                                "tentativas": contador,
                                "numero_sorteado": numero_sorteado,
                                "dificuldade": "Médio",
                                "data": data_formatada
                            })

                            with open(arquivo, "w", encoding="utf-8") as f:
                                json.dump(ranking, f, indent=4, ensure_ascii=False)

                            input("Pressione ENTER para continuar...") 
                            return         
                        else:
                            print("Você ainda não acertou o número, tente novamente")
                            print("tentativas: ", contador)
                            if numero_escolido > numero_sorteado:
                                print("O número escolhido é maior.")
                                input("Pressione ENTER para continuar...")
                            else:
                                print("O número escolhido é menor")
                                input("Pressione ENTER para continuar...")
                            limpar_tela()
                    except ValueError:
                        print("Escolha uma opção válida!")
                        input("Pressione ENTER para continuar...")
                        continue
            
            
            case 3: 
                limpar_tela()
                print("Você escolheu a opção Dificil")
                numero_sorteado = random.randint(1,500)
                while True:
                    nome_usuario = input("Para iniciar insira o seu nome por favor: ")

                    if len(nome_usuario) == 0:
                        print("Nome do usuário não pode ser vazio")
                    else:
                        break
                
                contador = 0
                print("Agora o jogo está iniciando")
                while True:
                    contador +=1
                    try:
                        numero_escolido = int(input("Escolha uma opção: "))
                        data_atual = datetime.now()
                        data_formatada = data_atual.strftime("%d/%m/%y %H:%M:%S")
                        if numero_sorteado == numero_escolido:
                            print(f"Parabéns você acertou {nome_usuario}, você acertou o número sorteado que foi, {numero_sorteado} com {contador} tentativas") 
                            arquivo = os.path.join("projeto", "ranking.json")

                            if not os.path.exists(arquivo):
                                with open(arquivo, "w", encoding="utf-8") as f:
                                    json.dump([], f, indent=4, ensure_ascii=False)

                            with open(arquivo, "r", encoding="utf-8") as f:
                                ranking = json.load(f)

                            ranking.append({
                                "nome": nome_usuario,
                                "tentativas": contador,
                                "numero_sorteado": numero_sorteado,
                                "dificuldade": "Dificil",
                                "data": data_formatada
                            })

                            with open(arquivo, "w", encoding="utf-8") as f:
                                json.dump(ranking, f, indent=4, ensure_ascii=False)

                            input("Pressione ENTER para continuar...") 
                            return         
                        else:
                            print("Você ainda não acertou o número, tente novamente")
                            print("tentativas: ", contador)
                            if numero_escolido > numero_sorteado:
                                print("O número escolhido é maior.")
                                input("Pressione ENTER para continuar...")
                            else:
                                print("O número escolhido é menor")
                                input("Pressione ENTER para continuar...")
                            limpar_tela()
                    except ValueError:
                        print("Escolha uma opção válida!")
                        input("Pressione ENTER para continuar...")
                        continue
            case 4:
                return
            case _:
                print("Escolha um opção válida")
        
