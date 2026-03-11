import os
import jogar
import historico
import ranking
import estatisticas

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    limpa_tela()

    print("Você acaba de entrar em um jogo de adivinhação")
    print("----------------------------------------------")
    print("Escolha uma das opções abaixo:")
    print("1- Jogar")
    print("2- Ver Ranking")
    print("3- Ver Histórico")
    print("4- Ver Estatísticas")
    print("5- Sair")

    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Escolha uma opção válida!")
        input("Pressione ENTER para continuar...")
        continue

    match escolha:

        case 1:
            limpa_tela()
            jogar.jogar()

        case 2:
            limpa_tela()
            print("Você escolheu ver o ranking")
            ranking.ranking()
            input("Pressione ENTER para continuar...")


        case 3:
            limpa_tela()
            print("Você escolheu ver histórico")
            historico.historico()
            input("Pressione ENTER para continuar...")

        case 4:
            limpa_tela()
            print("Você escolheu ver estatísticas")
            estatisticas.estatisticas()
            input("Pressione ENTER para continuar...")

        case 5:
            print("Saindo do jogo...")
            break

        case _:
            print("Escolha uma opção válida")

    