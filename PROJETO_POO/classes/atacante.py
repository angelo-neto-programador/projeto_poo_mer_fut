from classes.jogador import Jogador  # Importa a classe base Jogador

# Herança
class Atacante(Jogador):
    def __init__(self, nome, idade, valor_mercado, gols_marcados):
        super().__init__(nome, "Atacante", idade, valor_mercado)  # Chama o construtor da classe base
        self._gols_marcados = gols_marcados  # Encapsulamento: atributo protegido

    # Polimorfismo: Sobrescreve o método atualizar_valor_mercado
    def atualizar_valor_mercado(self, desempenho):
        # Atacantes aumentam o valor de mercado com base nos gols marcados
        self._valor_mercado += desempenho * 2  # Cada gol aumenta o valor em €2M
        print(f"Atacante {self._nome} marcou {desempenho} gols. Valor de mercado atualizado para €{self._valor_mercado}M")