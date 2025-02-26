# Projeto de Mercado de Futebol em POO

Este projeto demonstra os conceitos de **Programação Orientada a Objetos (POO)** usando o tema do mercado de futebol. Ele simula jogadores, clubes, transferências e contratos, aplicando os pilares da POO: **Abstração**, **Encapsulamento**, **Herança** e **Polimorfismo**.

---

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos e pastas:

/projeto_mercado_futebol
│
├── main.py # Arquivo principal para executar o programa
├── classes/ # Pasta com as classes do projeto
│ ├── init.py # Arquivo para tornar a pasta um pacote
│ ├── jogador.py # Classe Jogador (classe base)
│ ├── atacante.py # Classe Atacante (herda de Jogador)
│ ├── meio_campista.py # Classe MeioCampista (herda de Jogador)
│ └── goleiro.py # Classe Goleiro (herda de Jogador)
├── funcoes/ # Pasta com funções auxiliares
│ ├── init.py # Arquivo para tornar a pasta um pacote
│ └── utils.py # Funções utilitárias
└── README.md # Documentação do projeto


---

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto_mercado_futebol.git

2. Navegue até a pasta do projeto:
   cd projeto_mercado_futebol

3.Execute o arquivo principal:
  python main.py

---

Funcionalidades do Projeto:
O projeto simula o mercado de futebol com as seguintes funcionalidades:

Jogadores:
- Cada jogador tem um nome, posição, idade e valor de mercado.
- O valor de mercado pode ser atualizado com base no desempenho (gols, assistências, defesas).

Conceitos de POO Aplicados:

1. Abstração:
   A classe **Jogador** representa um conceito geral de um jogador de futebol, com atributos e métodos comuns.
   Ex:
   class Jogador:
    def __init__(self, nome, posicao, idade, valor_mercado):
        self._nome = nome
        self._posicao = posicao
        self._idade = idade
        self._valor_mercado = valor_mercado

   2. Encapsulamento:
      Atributos como _nome, _posicao, _idade e _valor_mercado são protegidos com _.

      Métodos públicos (get_nome, get_valor_mercado) permitem acesso controlado aos atributos.

      Ex:
      def get_nome(self):
    return self._nome

    3. Herança:
       As subclasses Atacante, MeioCampista e Goleiro herdam atributos e métodos da classe base Jogador.
       Ex:
       class Atacante(Jogador):
    def __init__(self, nome, idade, valor_mercado, gols_marcados):
        super().__init__(nome, "Atacante", idade, valor_mercado)
        self._gols_marcados = gols_marcados
