import os
import json
def ranking():
    
    def mostrar_ranking(ranking, dificuldade):
        filtrado = [j for j in ranking if j["dificuldade"] == dificuldade]

        if len(filtrado) == 0:
            print(f"Nenhum jogador jogou ainda no ranking {dificuldade.lower()}")
            return

        filtrado.sort(key=lambda x: x["tentativas"])

        print(f"Ranking {dificuldade}:")
        for indice, jogador in enumerate(filtrado[:10], start=1):
            print(f"{indice}° - {jogador['nome']} - {jogador['tentativas']} tentativas")

    arquivo = os.path.join("projeto", "ranking.json")

    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)


    with open(arquivo, "r", encoding="utf-8") as f:
        ranking = json.load(f)

    mostrar_ranking(ranking, "Fácil")
    print()
    mostrar_ranking(ranking, "Médio")
    print()
    mostrar_ranking(ranking, "Dificil")