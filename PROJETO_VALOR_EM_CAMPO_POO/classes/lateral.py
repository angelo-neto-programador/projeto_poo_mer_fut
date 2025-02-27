from classes.jogador import Jogador

class Lateral(Jogador):
    def __init__(self, nome, idade, valor_mercado, cruzamentos_certos):
        super().__init__(nome, "Lateral", idade, valor_mercado)
        self._cruzamentos_certos = cruzamentos_certos

    def atualizar_valor_mercado(self, desempenho):
        # Laterais aumentam o valor de mercado com base nos cruzamentos certos
        self._valor_mercado += desempenho * 0.7  # Cada cruzamento certo aumenta o valor em €0.7M
        print(f"Lateral {self._nome} fez {desempenho} cruzamentos certos. Valor de mercado atualizado para €{self._valor_mercado}M")

    def diminuir_valor_mercado(self, desempenho_negativo):
        # Laterais perdem valor de mercado com base em cruzamentos errados
        self._valor_mercado -= desempenho_negativo * 0.5  # Cada cruzamento errado diminui o valor em €500.000
        print(f"Lateral {self._nome} errou {desempenho_negativo} cruzamentos. Valor de mercado diminuído para €{self._valor_mercado}M")