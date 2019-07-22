#!/usr/bin/env python3

# @author: danbros
# Tarefa S6 em Introdução à CC com Python I USP (Coursera)
""" NIM game 

Um simples jogo de NIM invencível usando teoria dos jogos
"""


def computador_escolhe_jogada(n: int, m: int) -> int:
    """Escolhe quantas pilhas o algoritmo deve retirar

    Args:
      n: Número de "pilhas" do jogo
      m: Número máximo de pilhas a ser retirados.

    Returns:
        int: Resto dos múltiplos (m + 1) 
    """
    return n % (m + 1)


def usuario_escolhe_jogada(n: int, m: int) -> int:
    """

    Args:
      n: Número de "pilhas" do jogo
      m: Número máximo de pilhas a ser retirados. 

    Returns:
        int: Número de pilhas do usuário
    """
    while True:
        ans = int(input('\nQuantas peças você vai tirar? '))
        if ans < 1 or ans > m or ans > n:
            print('\nOops! Jogada inválida! Tente de novo.')
        else:
            return ans


def partida():
    """Comanda o andamento do jogo até o fim"""
    n = int(input('\nQuantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    flag = True

    if n % (m + 1) == 0:
        print('\nVoce começa!')
    else:
        print('\nComputador começa!')
        flag = False

    while True:
        if flag:
            ans = usuario_escolhe_jogada(n, m)
            if ans == 1:
                print('\nVocê tirou uma peça.')
            else:
                print(f'Você tirou {ans} peças.')
            flag = False
        else:
            ans = computador_escolhe_jogada(n, m)
            if ans == 1:
                print('\nO computador tirou uma peça.')
            else:
                print(f'\nO computador tirou {ans} peças.')
            flag = True

        n = n - ans

        if n < 2:
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            else:
                print('Fim do jogo! O computador ganhou!')
                break
        else:
            print(f'Agora restam {n} peças no tabuleiro.')


def campeonato():
    """Chama partida 3 vezes"""
    for i in range(1, 4):
        print(f'\n**** Rodada {i} ****')
        partida()


def NIM_game():
    """Main"""
    print('Bem-vindo ao jogo do NIM! Escolha:\n')
    print('1 - para jogar uma partida isolada')
    option = int(input('2 - para jogar um campeonato '))

    if option == 1:
        print('\nVoce escolheu uma partida isolada!\n')
        partida()
    else:
        print('\nVoce escolheu um campeonato!')
        campeonato()
        print('\n**** Final do campeonato! ****')
        print('Placar: Você 0 X 3 Computador')

if __name__ == "__main__":
    NIM_game()