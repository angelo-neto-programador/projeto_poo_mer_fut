from classes.jogador import Jogador  

class Goleiro(Jogador):
    def __init__(self, nome, idade, valor_mercado, defesas):
        super().__init__(nome, "Goleiro", idade, valor_mercado)  
        self._defesas = defesas  

    def atualizar_valor_mercado(self, desempenho):
        # Goleiros aumentam o valor de mercado com base nas defesas
        self._valor_mercado += desempenho * 1  # Cada defesa aumenta o valor em €1M
        print(f"Goleiro {self._nome} fez {desempenho} defesas. Valor de mercado atualizado para €{self._valor_mercado}M")

    def diminuir_valor_mercado(self, gols_erro):
        # Goleiros perdem valor de mercado por gols sofridos devido a erros
        self._valor_mercado -= gols_erro * 1.2  # Cada gol por erro diminui o valor em €1.2M
        print(f"Goleiro {self._nome} sofreu {gols_erro} gols por erro. Valor de mercado diminuído para €{self._valor_mercado}M")