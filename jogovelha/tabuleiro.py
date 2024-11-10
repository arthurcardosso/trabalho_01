

class Tabuleiro:
    """Representa o tabuleiro do jogo da velha.

    Args:
        casas (list[list[str]]): Matriz 3x3 que representa as casas do tabuleiro,
        onde cada casa pode estar vazia (' ') ou conter um símbolo ('X' ou 'O').

    Methods:
        __init__() -> None: Inicializa o tabuleiro com todas as casas vazias.
        pegar_tabuleiro() -> list[list[str]]: Retorna o estado atual do tabuleiro.
        marcar_casa(lance: tuple[int, int], simbolo: str) -> None: Marca uma casa do
        tabuleiro com o símbolo fornecido, caso esteja disponível. Caso contrário, levanta um erro.
        imprimir_tabuleiro() -> None: Imprime o tabuleiro no console,
        exibindo as linhas, colunas e seus respectivos símbolos.
    """


    def __init__(self) -> None:
        """Inicializa o tabuleiro com todas as casas vazias.
        """
        self.casas = [[' ' for i in range(3)] for i in range (3)]

    def pegar_tabuleiro(self) -> list[list[str]]:
        """Retorna o estado atual do tabuleiro.

        Returns:
            list[list[str]]: O estado atual do tabuleiro, representado por uma
            matriz 3x3 de strings (' ' para vazio, 'X' ou 'O' para símbolos).
        """
        return self.casas

    def marcar_casa(self, lance: tuple[int, int], simbolo: str) -> None:
        """Marca uma casa do tabuleiro de acordo com o símbolo fornecido.

        Args:
            lance (tuple[int, int]): As coordenadas da casa a ser marcada (linha, coluna).
            simbolo (str): O símbolo a ser inserido na casa ('X' ou 'O').

        Raises:
            ValueError: Se a casa já estiver ocupada.
        """
        if self.casas[lance[0]][lance[1]] == ' ':
            self.casas[lance[0]][lance[1]] = simbolo
        else:
            raise ValueError('Tente Novamente! Essa casa já está ocupada.')

    def imprimir_tabuleiro(self) -> None:
        """Imprime o tabuleiro no terminal, exibindo linhas, colunas e seus símbolos.

        Exibe o tabuleiro atual, numerando as colunas e as linhas para facilitar
        a identificação das casas para os jogadores.
        """
        print()
        print("    0   1   2")
        for coluna, linha in enumerate(self.casas):
            print(f"{coluna} | {' | '.join(linha)} |")
            if coluna < 2:
                print("  ─────────────")
        print()
