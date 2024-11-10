from abc import ABC, abstractmethod
import random


class Jogador(ABC):
    """Classe base para um jogador no jogo da velha.

    Atributos:
        simbolo (str): O símbolo do jogador ('X' ou 'O').

    Métodos:
        __init__(simbolo: str) -> None: Inicializa o jogador com um símbolo.
        fazer_jogada(tabuleiro) -> tuple[int, int]: Método abstrato que deve ser
        implementado pelas subclasses para definir como o jogador faz seu lance.
    """

    def __init__(self, simbolo: str) -> None:
        """Inicializa o jogador com o símbolo fornecido.

        Args:
            simbolo (str): O símbolo do jogador ('X' ou 'O').
        """
        self.simbolo = simbolo

    def fazer_jogada(self, tabuleiro) -> tuple[int, int]:
        """Define o comportamento do jogador ao fazer uma jogada.

        Args:
            tabuleiro (Tabuleiro): A instância do tabuleiro onde o jogador
            realizará a jogada.

        Returns:
            tuple[int, int]: As coordenadas da jogada no formato (linha, coluna).
        """
        pass


class JogadorHumano(Jogador):
    """Representa um jogador humano no jogo da velha.

    Methods:
        fazer_jogada(tabuleiro) -> tuple[int, int]: Solicita ao jogador que informe
        uma posição para realizar a jogada.
    """

    def fazer_jogada(self, tabuleiro) -> tuple[int, int]:
        """Solicita ao jogador humano a entrada de uma jogada.

        Exibe uma mensagem solicitando a entrada no formato "linha, coluna". O jogador
        deve inserir uma posição válida. Se a entrada for inválida, o jogador será
        solicitado a tentar novamente até que uma jogada válida seja fornecida.

        Args:
            tabuleiro (Tabuleiro): A instância do tabuleiro onde o jogador
            realizará a jogada.

        Returns:
            tuple[int, int]: As coordenadas da jogada no formato (linha, coluna).
        """
        print()
        print(f'Jogador ({self.simbolo}), é a sua vez!')
        while True:
            try:
                entrada = input('Informe a posição do seu lance (Linha, Coluna): ')
                linha, coluna = map(int, entrada.split(','))
                if tabuleiro.casas[linha][coluna] == ' ':
                    return (linha, coluna)
                else:
                    print('Essa casa já está ocupada!')

            except (ValueError, IndexError):
                print('A Entrada é inválida!')
                print('Certifique-se de que está no formato correto e dentro dos limites (0, 1, 2).')


class JogadorComputador(Jogador):
    """Representa um jogador computador no jogo da velha.

    Args:
        estrategia (str): A estratégia usada pelo jogador computador. Atualmente,
        apenas a estratégia 'aleatoria' é suportada.

    Methods:
        __init__(simbolo: str, estrategia: str = 'aleatoria') -> None: Inicializa o jogador computador.
        fazer_jogada(tabuleiro) -> tuple[int, int]: Faz uma jogada aleatória.
    """

    def __init__(self, simbolo: str, estrategia: str = 'aleatoria') -> None:
        """Inicializa o jogador computador com um símbolo e estratégia.

        Args:
            simbolo (str): O símbolo do jogador computador ('X' ou 'O').
            estrategia (str): A estratégia de jogada do computador. Padrão é 'aleatoria'.

        Raises:
            ValueError: Se a estratégia fornecida for inválida.
        """
        super().__init__(simbolo)
        self.estrategia = estrategia
        if estrategia not in ['aleatoria']:
            raise ValueError('A Estratégia é Inválida! Use "aleatoria". ')

    def fazer_jogada(self, tabuleiro) -> tuple[int, int]:
        """Faz uma jogada aleatória no tabuleiro.

        Seleciona uma posição vazia no tabuleiro de forma aleatória e retorna as
        coordenadas da jogada.

        Args:
            tabuleiro (Tabuleiro): A instância do tabuleiro onde o jogador computador
            realizará a jogada.

        Returns:
            tuple[int, int]: As coordenadas do lance no formato (linha, coluna).
        """
        if self.estrategia == 'aleatoria':
            jogadas_possiveis = [ (i, j) for i in range(3) for j in range(3) if tabuleiro.casas[i][j] == ' ']
            return random.choice(jogadas_possiveis)
