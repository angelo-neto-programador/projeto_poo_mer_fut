# Projeto Valor em Campo POO

Descrição:
Este projeto é um sistema de gerenciamento de jogadores de futebol, desenvolvido em Python, que utiliza conceitos de Programação Orientada a Objetos (POO), como Abstração, Encapsulamento, Herança e Polimorfismo. O sistema permite criar jogadores de diferentes posições (Atacante, Meio-Campista, Goleiro, Lateral e Zagueiro), atualizar seus valores de mercado com base no desempenho e diminuir o valor de mercado em caso de desempenhos negativos.

---

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos e pastas:

/projeto_valor_em_campo

├── main.py                # Arquivo principal para executar o programa
├── classes/               # Pasta com as classes do projeto
│   ├── jogador.py         # Classe Jogador (classe base)
│   ├── atacante.py        # Classe Atacante (herda de Jogador)
│   ├── meio_campista.py   # Classe MeioCampista (herda de Jogador)
│   └── goleiro.py         # Classe Goleiro (herda de Jogador)
│   └── zagueiro.py         # Classe Zagueiro (herda de Jogador)
│   └── lateral.py         # Classe Lateral (herda de Jogador)
└── README.md              # Documentação do projeto


---

**Como Executar o Projeto**

Pré-requisitos
1 - Python 3.12: Certifique-se de ter o Python instalado em sua máquina.

2 - IDE ou Editor de Texto: Recomendo o uso do VS Code, PyCharm ou qualquer editor de sua preferência.

Passo a Passo
1 - Clone o repositório (se estiver usando Git) ou baixe os arquivos do projeto.

2 - Navegue até a pasta do projeto:
cd caminho/para/PROJETO_VALOR_EM_CAMPO_POO

3 - Execute o arquivo main.py:
python main.py

4 - Saída Esperada:
O programa exibirá informações sobre os jogadores, atualizará seus valores de mercado com base no desempenho e diminuirá o valor em caso de desempenhos negativos.

Explicação do Código

1. Classe Base: **Jogador**

A classe **Jogador** é a base para todas as outras classes. Ela define os atributos comuns a todos os jogadores, como nome, posição, idade e valor de mercado, e métodos para acessar esses atributos.

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

2. Classes Específicas: Atacante, MeioCampista, Goleiro, Lateral, Defensor

Cada classe herda da classe Jogador e adiciona atributos e comportamentos específicos para cada posição.

Código: atacante.py

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

Código: meio_campista.py

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

Código: goleiro.py

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

Código: lateral.py

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

Código: zagueiro.py

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

3. Execução do Projeto: main.py

O arquivo main.py cria instâncias dos jogadores e testa as funcionalidades.

    Código: main.py

    from classes.atacante import Atacante
    from classes.meio_campista import MeioCampista
    from classes.goleiro import Goleiro
    from classes.lateral import Lateral
    from classes.defensor import Defensor

    def definir_jogador(jogador, desempenho):
        print(f"\nDefinindo {jogador.__class__.__name__}:")
        jogador.exibir_info()
        jogador.atualizar_valor_mercado(desempenho)

    def diminuir_valor_jogador(jogador, desempenho_negativo):
        print(f"\nDiminuindo valor de mercado de {jogador.__class__.__name__}:")
        jogador.exibir_info()
        jogador.diminuir_valor_mercado(desempenho_negativo)

    if __name__ == "__main__":
        # Instâncias de jogadores
        neymar = Atacante("Neymar", 31, 80, 200)
        modric = MeioCampista("Modric", 37, 50, 150)
        neuer = Goleiro("Neuer", 30, 70, 100)
        marcelo = Lateral("Marcelo", 34, 30, 50)
        ramos = Defensor("Ramos", 36, 40, 80)

    # Testa os jogadores com diferentes desempenhos
    definir_jogador(neymar, 10)  # Neymar marcou 10 gols
    definir_jogador(modric, 8)  # Modric deu 8 assistências
    definir_jogador(neuer, 15)  # Neuer fez 15 defesas
    definir_jogador(marcelo, 10)  # Marcelo fez 10 cruzamentos certos
    definir_jogador(ramos, 20)  # Ramos fez 20 desarmes certos

    # Testa a diminuição do valor de mercado
    diminuir_valor_jogador(neymar, 5)  # Neymar ficou 5 jogos sem marcar
    diminuir_valor_jogador(modric, 4)  # Modric ficou 4 jogos sem assistências
    diminuir_valor_jogador(neuer, 3)  # Neuer sofreu 3 gols por erro
    diminuir_valor_jogador(marcelo, 4)  # Marcelo teve 4 desempenhos negativos
    diminuir_valor_jogador(ramos, 6)  # Ramos teve 6 desempenhos negativos
----------

Resultado esperado:

**Definindo Atacante:
Atacante Neymar marcou 10 gols. Valor de mercado atualizado para €35M

Definindo MeioCampista:
Meio-Campista Modric deu 8 assistências. Valor de mercado atualizado para €17.0M

Definindo Goleiro:
Goleiro Neuer fez 15 defesas. Valor de mercado atualizado para €19M

Definindo Lateral:
Lateral Lucas Piton fez 10 cruzamentos certos. Valor de mercado atualizado para €15.0M

Definindo Zagueiro:
Zagueiro Ramos fez 2 desarmes certos. Valor de mercado atualizado para €2.8M

Diminuindo valor de mercado de Atacante:
Atacante Neymar ficou 5 jogos sem marcar. Valor de mercado diminuido para €30M

Diminuindo valor de mercado de MeioCampista:
Meio-Campista Modric ficou 4 jogos sem assistências. Valor de mercado diminuido para €13.8M

Diminuindo valor de mercado de Goleiro:
Goleiro Neuer sofreu 3 gols por erro. Valor de mercado diminuido para €15.4M

Diminuindo valor de mercado de Lateral:
Lateral Lucas Piton errou 4 cruzamentos. Valor de mercado diminuido para €13.0M

Diminuindo valor de mercado de Zagueiro:
Zagueiro Ramos fez 6 botes errados na bola. Valor de mercado diminuido para €1.0M**


**Versão do Projeto**:
- Versão 1.0.0: Lançamento inicial do projeto

**Changelog**:
- v1.0.0(27/02/2025):
- Implementação das classes Jogador, Atacante, MeioCampista, Goleiro, Lateral e Zagueiro.
- Adicionada funcionalidade de atualização e diminuição do valor de mercado.

**Autor**:
- Angelo Neto

**Contato**:
Email: angeloneto@alu.ufc.br

**Agradecimentos**:
- Agradeço a toda a comunidade da Universidade Federal do Ceará por todo o suporte e inspiração.
- Um agradecimento especial ao Professor Juan Sebastian Toquica Arenas pelo seu trabalho ensinando os métodos de Progamação Orientada a Objetos para toda a comunidade discente.
