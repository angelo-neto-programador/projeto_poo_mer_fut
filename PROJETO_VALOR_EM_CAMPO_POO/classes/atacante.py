from classes.jogador import Jogador  

class Atacante(Jogador):
    def __init__(self, nome, idade, valor_mercado, gols_marcados):
        super().__init__(nome, "Atacante", idade, valor_mercado)  
        self._gols_marcados = gols_marcados  

    def atualizar_valor_mercado(self, desempenho):
        # Atacantes aumentam o valor de mercado com base nos gols marcados
        self._valor_mercado += desempenho * 2  # Cada gol aumenta o valor em €2M
        print(f"Atacante {self._nome} marcou {desempenho} gols. Valor de mercado atualizado para €{self._valor_mercado}M")

    def diminuir_valor_mercado(self, jogos_sem_gol):
        # Atacantes perdem valor de mercado por jogos sem marcar gols
        self._valor_mercado -= jogos_sem_gol * 1  # Cada jogo sem gol diminui o valor em €1M
        print(f"Atacante {self._nome} ficou {jogos_sem_gol} jogos sem marcar. Valor de mercado diminuído para €{self._valor_mercado}M")