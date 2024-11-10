"""Setup.py do Pacote

Script de configuração para o pacote 'JogoVelha'. Esse arquivo usa a função
'setup' do módulo 'setuptools' para definir as informações do pacote e suas dependências.

Functions:
    setup: Configura o pacote com nome, versão, descrição, autor, dependências,
    e outros metadados necessários para distribuição.

Args:
    name (str): O nome do pacote.
    version (str): A versão atual do pacote.
    description (str): Uma breve descrição do pacote.
    long_description (str): Descrição mais detalhada, lida do arquivo 'README.md'.
    long_description_content_type (str): O formato do arquivo de descrição longa, neste caso, Markdown.
    author (str): Nome do autor do pacote.
    author_email (str): Email do autor para contato.
    python_requires (str): Versão mínima do Python necessária para rodar o pacote.
    packages (list): Pacotes que serão incluídos na distribuição.
    install_requires (list): Dependências necessárias para rodar o pacote.
    license (str): A licença sob a qual o pacote é distribuído.
    keywords (list): Palavras-chave que descrevem o pacote.
    classifiers (list): Classificações adicionais para o pacote.
"""

from setuptools import setup, find_packages

setup(
    name='Jogo_da_Velha',
    version='1.0.0',
    description='Pacote para implementação de um jogo da velha codificado em Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arthur Cardoso',
    author_email='arthnrcardoso@gmail.com',
    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=[],
    license='MIT',
    keywords=['Jogo da Velha', 'Pacote de Implementação', 'Jogador', 'Tabuleiro'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
