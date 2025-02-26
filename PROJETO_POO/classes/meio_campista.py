from classes.jogador import Jogador  # Importa a classe base Jogador


class MeioCampista(Jogador):
    def __init__(self, nome, idade, valor_mercado, assistencias):
        super().__init__(nome, "Meio-Campista", idade, valor_mercado)  # Chama o construtor da classe base
        self._assistencias = assistencias  # Encapsulamento: atributo protegido

    # Polimorfismo: Sobrescreve o método atualizar_valor_mercado
    def atualizar_valor_mercado(self, desempenho):
        # Meio-campistas aumentam o valor de mercado com base nas assistências
        self._valor_mercado += desempenho * 1.5  # Cada assistência aumenta o valor em €1.5M
        print(f"Meio-Campista {self._nome} deu {desempenho} assistências. Valor de mercado atualizado para €{self._valor_mercado}M")