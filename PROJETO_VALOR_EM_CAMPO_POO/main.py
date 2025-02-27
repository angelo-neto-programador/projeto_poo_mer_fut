from classes.atacante import Atacante
from classes.meio_campista import MeioCampista
from classes.goleiro import Goleiro
from classes.lateral import Lateral
from classes.zagueiro import Zagueiro

def definir_jogador(jogador, desempenho):
    print(f"\nDefinindo {jogador.__class__.__name__}:")
    jogador.exibir_info()
    jogador.atualizar_valor_mercado(desempenho)

def diminuir_valor_jogador(jogador, desempenho_negativo):
    print(f"\nDiminuindo valor de mercado de {jogador.__class__.__name__}:")
    jogador.exibir_info()
    jogador.diminuir_valor_mercado(desempenho_negativo)

if __name__ == "__main__":
    # Instâncias de jogadores
    neymar = Atacante("Neymar", 33, 15, 437)
    modric = MeioCampista("Modric", 39, 5, 150)
    neuer = Goleiro("Neuer", 38, 4, 720)
    piton = Lateral("Lucas Piton", 24, 8, 119)
    ramos = Zagueiro("Ramos", 38, 1.80, 320)

    # Testa os jogadores com diferentes desempenhos
    definir_jogador(neymar, 10)      # Neymar marcou 10 gols
    definir_jogador(modric, 8)       
    definir_jogador(neuer, 15)       
    definir_jogador(piton, 10)     
    definir_jogador(ramos, 2)       # Ramos fez 20 desarmes certos

    # Testa a diminuição do valor de mercado
    diminuir_valor_jogador(neymar, 5)       # Neymar ficou 5 jogos sem marcar
    diminuir_valor_jogador(modric, 4)       
    diminuir_valor_jogador(neuer, 3)        
    diminuir_valor_jogador(piton, 4)      #Marcelo errou 4 cruzamentos
    diminuir_valor_jogador(ramos, 6)        #Ramos errou 6 botes na bola