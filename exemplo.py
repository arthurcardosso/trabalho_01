"""Exemplo de Uso do Pacote

Exemplo de execução de um jogo da velha utilizando as classes 'JogoVelha',
'JogadorHumano' e 'JogadorComputador' do módulo 'jogovelha'.

Classes:
    JogadorHumano: Representa um jogador humano no jogo da velha.
    JogadorComputador: Representa um jogador controlado pelo computador no jogo da velha.
    JogoVelha: Implementa a lógica principal do jogo da velha.

Examples:
    O código cria dois jogadores, um humano e um computador, e inicializa uma
    instância do jogo da velha. Em seguida, o jogo é executado através do método 'jogar'.

    jogador1 = JogadorHumano('X')
    jogador2 = JogadorComputador('O', 'aleatoria')
    jogo = JogoVelha(jogador1, jogador2)
    jogo.jogar()
"""

from jogovelha import JogoVelha, JogadorHumano, JogadorComputador

jogador1 = JogadorHumano('X')
jogador2 = JogadorComputador('O', 'aleatoria')
jogo = JogoVelha(jogador1, jogador2)
jogo.jogar()
