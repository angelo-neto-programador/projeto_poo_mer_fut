from classes.jogador import Jogador  


class Zagueiro(Jogador):
    def __init__(self, nome, idade, valor_mercado, defesas):
        super().__init__(nome, "Zagueiro", idade, valor_mercado)  
        self._defesas = defesas  
        
    # Polimorfismo: Sobrescreve o método atualizar_valor_mercado
    def atualizar_valor_mercado(self, desempenho):
        # zagueiros aumentam o valor de mercado com base nos botes acertados
        self._valor_mercado += desempenho * 1        # Cada bote acertado aumenta o valor em €1M
        print(f"Zagueiro {self._nome} acertou {desempenho} botes certos. Valor de mercado atualizado para €{self._valor_mercado}M")
