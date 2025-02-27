from classes.jogador import Jogador  

class MeioCampista(Jogador):
    def __init__(self, nome, idade, valor_mercado, assistencias):
        super().__init__(nome, "Meio-Campista", idade, valor_mercado) 
        self._assistencias = assistencias  

    def atualizar_valor_mercado(self, desempenho):
        # Meio-campistas aumentam o valor de mercado com base nas assistências
        self._valor_mercado += desempenho * 1.5  # Cada assistência aumenta o valor em €1.5M
        print(f"Meio-Campista {self._nome} deu {desempenho} assistências. Valor de mercado atualizado para €{self._valor_mercado}M")

    def diminuir_valor_mercado(self, jogos_sem_assistencia):
        # Meio-campistas perdem valor de mercado por jogos sem dar assistências
        self._valor_mercado -= jogos_sem_assistencia * 0.8  # Cada jogo sem assistência diminui o valor em €0.8M
        print(f"Meio-Campista {self._nome} ficou {jogos_sem_assistencia} jogos sem assistências. Valor de mercado diminuído para €{self._valor_mercado}M")