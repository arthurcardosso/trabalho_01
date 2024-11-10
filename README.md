
# Jogo da Velha (Pacote 'jogovelha')

Este projeto implementa um jogo da velha desenvolvido em Python como um pacote
reutilizável. O jogo permite jogar contra outra jogador humano ou contra um
computador controlado por uma estratégia aleatória.

## Índice

- *Descrição do Projeto*
- *Componentes do Projeto*
- *Instalação*
- *Uso*
- *Estrutura do Pacote*
- *Funcionalidade*
- *Dependências*
- *Licença*
- *Contato*
- *Agradecimentos*

## Descrição do Projeto

Esse pacote contém uma implementação simples de um jogo da velha, onde dois jogadores competem entre
si. O jogador pode escolher entre jogar contra outro jogador humano ou contra um "computador virtual"
controlada por uma estratégia aleatória que simula um jogador. Além disso, o jogo segue as mesmas regras
e definições usuais de um jogo da velha clássico.

## Componentes do Projeto

- **JogoVelha**: Classe principal que gerencia o jogo.
- **Tabuleiro**: Classe que representa o tabuleiro de jogo.
- **Jogador**: Classe abstrata para os diferentes tipos de jogadores.
- **JogadorHumano**: Subclasse responsável pela implementação de um jogador humano.
- **JogadorComputador**: Subclasse responsável pela implementação de um jogador computador.

## Instalação

### 1. Clonando o Repositório
Primeiramente, clone o repositório para o seu ambiente local:

_git clone https://github.com/arthurcardosso/jogovelha.git_

### 2. Diretório do Projeto
Após isso, navegue até o diretório do projeto e digite:

_cd jogovelha_

### 3. Instalando o Projeto
Por fim, instale o projeto e suas dependências através do pip:

_pip install -e_

## Uso

Após a instalação, você pode usar o pacote diretamente ou como um módulo.

### Exemplo Uso da Implementação com outro jogador humano:

from jogovelha import JogoVelha, JogadorHumano, JogadorHumano

jogador1 = JogadorHumano('X')
jogador2 = JogadorHumano('O')
jogo = JogoVelha(jogador1, jogador2)
jogo.jogar()

### Exemplo de Uso da Implementação contra o computador:

from jogovelha import JogoVelha, JogadorHumano, JogadorComputador

jogador1 = JogadorHumano('X')
jogador2 = JogadorComputador('O', 'aleatoria')
jogo = JogoVelha(jogador1, jogador2)
jogo.jogar()

Se ainda possuir dúvidas, abra o arquivo _exemplo.py_ para analisar mais um uso prático do pacote.

## Estrutura do Pacote

A estrutura do pacote é organizada da seguinte forma:

jogovelha/
│
├── jogovelha/
│   ├── __init__.py
│   ├── jogo_velha.py    _# Contém a classe principal do jogo e a lógica de execução_
│   ├── tabuleiro.py     _# Representa o estado do jogo em forma de uma grade 3x3_
│   ├── jogador.py       _# Define a classe abstrata Jogador e suas subclasses JogadorHumano e JogadorComputador_
│
├── exemplo.py           _# Exemplo de uso do pacote_
├── setup.py             _# Arquivo de configuração do pacote_
├── README.md            _# Documentação do projeto_
├── LICENSE              _# Licença do projeto_
├── requirements.txt     _# Dependências_
└── relations.txt        _# Relações entre as classes_


## Funcionalidade

- **JogoVelha** controla a mecânica do jogo, alternando os turnos e verificando se o jogo acabou.
- **Tabuleiro** representa o ambiente de jogo em forma de uma grade 3x3.
- **JogadorHumano** solicita jogadas ao usuário.
- **JogadorComputador** faz jogadas aleaórias com base na estratégia _aleatória_ pré-definida.

## Dependências

O Projeto depende apenas da biblioteca padrão de módulos do Python (versão 3.8 ou superior), onde utiliza
os módulos internos 'random' e 'abc' em sua estrutura.

## Licença

Esse projeto está licenciado sob a MIT License - veja o arquivo LICENSE.txt para mais detalhes.

## Contato

Se você tiver perguntas, sugestões ou feedback sobre o projeto, fique à vontade para entrar em contato comigo através dos
seguintes meios de contatos:

- Email: arthnrcardoso@gmail.com
- Whatszapp: +55 82 993825927
- GitHub: github.com/arthurcardosso

## Agradecimentos

Monitor, agradeço por dedicar seu tempo para explorar e corrigir esse meu projeto de Programação Orientada a Objetos. Sua contribuição, observações e sugestão são muito bem-vindas por mim!
