from classes.atacante import Atacante
from classes.meio_campista import MeioCampista
from classes.goleiro import Goleiro

def testar_jogador(jogador, desempenho):
    print(f"\nTestando {jogador.__class__.__name__}:")
    jogador.exibir_info()
    jogador.atualizar_valor_mercado(desempenho)

if __name__ == "__main__":
    # Cria instâncias de jogadores
    neymar = Atacante("Neymar", 31, 80, 200)
    modric = MeioCampista("Modric", 37, 50, 150)
    neuer = Goleiro("Neuer", 30, 70, 100)
    pedro = Atacante("Pedro", 27, 20, 100)

    # Testa os jogadores com diferentes desempenhos
    testar_jogador(neymar, 10)  # Neymar marcou 10 gols
    testar_jogador(modric, 8)  # Modric deu 8 assistências
    testar_jogador(neuer, 15)  # Alisson fez 15 defesas
    testar_jogador(pedro, 22)