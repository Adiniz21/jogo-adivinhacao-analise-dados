import os
import json

def historico():
    arquivo = os.path.join("projeto", "ranking.json")

    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)


    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    if len(dados) == 0: 
        print("Nenhum jogo foi criado ainda")
        return
    
    indice = 1
    for jogador in dados:
        print(indice)
        print(f"Nome do Jogador: {jogador["nome"]}")
        print(f'Tentativas: {jogador["tentativas"]}')
        print(f"Dificuldade: {jogador["dificuldade"]}")
        print(f"Data que foi jogado: {jogador["data"]}")
        print("")
        indice +=1


    
