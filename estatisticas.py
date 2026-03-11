import os
import json

def estatisticas():
    def mostrar_estatisticas(estatisticas, dificuldade):
        filtrado = [j for j in estatisticas if j["dificuldade"] == dificuldade]

        if len(filtrado) == 0:
            print(f"Nenhum jogador jogou ainda no ranking {dificuldade.lower()}")
            return
        
        print(f"Total de jogos na dificuldade {dificuldade}: {len(filtrado)}")
        total_tentativas = sum(j["tentativas"] for j in filtrado)
        media = total_tentativas / len(filtrado)
        print(f"Média de tentativas na dificuldade {dificuldade}: {media}")


    arquivo = os.path.join(os.path.dirname(__file__), "ranking.json")

    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)


    with open(arquivo, "r", encoding="utf-8") as f:
        estatisticas = json.load(f)

    total_partidas = len(estatisticas)
    total_tentativas = sum(j["tentativas"] for j in estatisticas)

    media = total_tentativas / len(estatisticas)

    print("Total de Partidas:", total_partidas)
    print("Média de tentativas:", media)

    print()
    mostrar_estatisticas(estatisticas, "Fácil")
    print()
    mostrar_estatisticas(estatisticas, "Médio")
    print()
    mostrar_estatisticas(estatisticas, "Dificil")