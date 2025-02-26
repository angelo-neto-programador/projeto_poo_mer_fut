# Abstração e Encapsulamento
class Jogador:
    def __init__(self, nome, posicao, idade, valor_mercado):
        self._nome = nome  # Encapsulamento: atributo protegido
        self._posicao = posicao
        self._idade = idade
        self._valor_mercado = valor_mercado

    # Métodos públicos para acessar atributos encapsulados
    def get_nome(self):
        return self._nome

    def get_posicao(self):
        return self._posicao

    def get_idade(self):
        return self._idade

    def get_valor_mercado(self):
        return self._valor_mercado

    # Polimorfismo: Método que pode ser sobrescrito
    def atualizar_valor_mercado(self, desempenho):
        self._valor_mercado += desempenho
        print(f"Valor de mercado de {self._nome} atualizado para €{self._valor_mercado}M")

    def exibir_info(self):
        return f"Jogador: {self._nome}, Posição: {self._posicao}, Idade: {self._idade}, Valor de Mercado: €{self._valor_mercado}M"