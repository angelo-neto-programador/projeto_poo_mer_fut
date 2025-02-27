from classes.jogador import Jogador

class Zagueiro(Jogador):
    def __init__(self, nome, idade, valor_mercado, desarmes_certos):
        super().__init__(nome, "Zagueiro", idade, valor_mercado)
        self._desarmes_certos = desarmes_certos

    def atualizar_valor_mercado(self, desempenho):
        # zagueiros aumentam o valor de mercado com base nos desarmes certos
        self._valor_mercado += desempenho * 0.5  # Cada desarme certo aumenta o valor em €0.5M
        print(f"Zagueiro {self._nome} fez {desempenho} desarmes certos. Valor de mercado atualizado para €{self._valor_mercado}M")

    def diminuir_valor_mercado(self, desempenho_negativo):
        # zageurios perdem valor de mercado com base em botes errados na bola
        self._valor_mercado -= desempenho_negativo * 0.3  
        print(f"Zagueiro {self._nome} fez {desempenho_negativo} botes errados na bola. Valor de mercado diminuído para €{self._valor_mercado}M")