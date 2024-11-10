from jogovelha.tabuleiro import Tabuleiro
from jogovelha.jogador import Jogador


class JogoVelha:
    """Representa o jogo da velha entre dois jogadores.

    Args:
        tabuleiro (Tabuleiro): Instância da classe Tabuleiro, que mantém o estado do tabuleiro.
        jogadores (list[Jogador]): Lista contendo os dois jogadores, onde cada jogador é uma instância da classe Jogador.
        turno (int): Indica o índice do jogador atual (0 ou 1).

    Methods:
        __init__(jogador1: Jogador, jogador2: Jogador) -> None: Inicializa o jogo com dois jogadores.
        jogar() -> None: Executa o jogo, alternando entre os jogadores até que haja um vencedor ou empate.
        checar_fim_de_jogo() -> str | None: Verifica se o jogo terminou, seja por vitória ou empate.
        jogador_atual() -> Jogador: Retorna o jogador que está realizando a jogada atual.
    """


    def __init__(self, jogador1: Jogador, jogador2: Jogador) -> None:
        """Inicializa o jogo com dois jogadores.

        Args:
            jogador1 (Jogador): O primeiro jogador do jogo.
            jogador2 (Jogador): O segundo jogador do jogo.
        """
        self.tabuleiro = Tabuleiro()
        self.jogadores = [jogador1, jogador2]
        self.turno = 0

    def jogar(self) -> None:
        """Executa o jogo, alternando entre os jogadores até que haja um vencedor ou empate.

        A cada turno, o jogador atual faz uma jogada, que é processada pelo método
        'fazer_jogada'. O tabuleiro é atualizado e impresso, e o estado do jogo é
        verificado após cada jogada.
        """
        while True:
            jogador_atual = self.jogador_atual()
            lance = jogador_atual.fazer_jogada(self.tabuleiro)
            self.tabuleiro.marcar_casa(lance, jogador_atual.simbolo)
            self.tabuleiro.imprimir_tabuleiro()
            resultado = self.checar_fim_de_jogo()
            if resultado:
                print(resultado)
                break
            self.turno = (self.turno + 1 ) % 2

    def checar_fim_de_jogo(self) -> str | None:
        """Verifica se o jogo terminou.

        Verifica se há uma linha, coluna ou diagonal com três símbolos iguais,
        indicando vitória. Também verifica se o tabuleiro está completo, indicando empate.

        Returns:
            str | None: Uma mensagem indicando o resultado do jogo, ou None se o jogo continuar.
        """
        tabuleiro = self.tabuleiro.pegar_tabuleiro()
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
                return f'Fim de Jogo! O Jogador {tabuleiro[i][0]} venceu!'
            if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
                return f'Fim de Jogo! O Jogador {tabuleiro[0][i]} venceu!'

        if tabuleiro[0][0] == tabuleiro [1][1] == tabuleiro[2][2] != ' ':
            return f'Fim de Jogo! O Jogador {tabuleiro[0][0]} venceu!'

        if tabuleiro[0][2] == tabuleiro [1][1] == tabuleiro[2][0] != ' ':
            return f'Fim de Jogo! O Jogador {tabuleiro[0][2]} venceu!'

        if all(cell != ' ' for linha in tabuleiro for cell in linha):
            return 'Fim de Jogo! Tivemos um empate!'
        return None

    def jogador_atual(self) -> Jogador:
        """Retorna o jogador que está realizando a jogada atual.

        Returns:
            Jogador: O jogador atual do jogo.
        """
        return self.jogadores[self.turno]
