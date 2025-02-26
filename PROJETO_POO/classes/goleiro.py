from classes.jogador import Jogador  

# Herança
class Goleiro(Jogador):
    def __init__(self, nome, idade, valor_mercado, defesas):
        super().__init__(nome, "Goleiro", idade, valor_mercado)  # Chama o construtor da classe base
        self._defesas = defesas  # Encapsulamento: atributo protegido

    # Polimorfismo: Sobrescreve o método atualizar_valor_mercado
    def atualizar_valor_mercado(self, desempenho):
        # Goleiros aumentam o valor de mercado com base nas defesas
        self._valor_mercado += desempenho * 1  # Cada defesa aumenta o valor em €1M
        print(f"Goleiro {self._nome} fez {desempenho} defesas. Valor de mercado atualizado para €{self._valor_mercado}M")
