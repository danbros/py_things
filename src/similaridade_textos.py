#!/usr/bin/env python3

# @author: danbros
# Tarefa S9 em Introdução à CC com Python I USP (Coursera)

""" Similaridade entre textos 

Este script permite ao usuário criar uma assinatura de um texto, e comparar a
similaridade entre textos.

Este arquivo também pode ser importado como um módulo.
"""

import re


def le_assinatura():
    """A funcao lê os valores dos tracos linguisticos do modelo e devolve uma
    assinatura a ser comparada com os textos fornecidos.

    Returns:
      list: Uma lista de números representando a assinatura a ser avaliada
    """

    print("\nBem-vindo ao detector automático de COH-PIAH.\n")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A função lê cada texto recebido até a entrada de um Enter

    Returns:
      list: Uma lista de strings com todos os textos de entrada.
    """
    i = 1
    texts = []
    text = input(f"\nDigite o texto {i} (aperte enter para sair): ")
    while text:
        texts.append(text)
        i += 1
        text = input(f"\nDigite o texto {i} (aperte enter para sair): ")

    return texts


def separa_sentencas(text: str) -> list:
    """A funcao recebe um txt e devolve uma lista das sentenças dentro do txt

    Args:
      text(str): O texto a ser dividido em sentenças
      text: str: 

    Returns:
      list: Uma lista de strings onde cada string é uma sentença
    """
    sentences = re.split(r'[.!?]+', text)
    if sentences[-1] == '':
        del sentences[-1]

    return sentences


def separa_frases(sentence: str) -> list:
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da
    sentenca

    Args:
      sentence(str): A sentença a ser dividida em frases

    Returns:
        list: Uma lista de strings onde cada string é uma frase
    """
    return re.split(r'[,:;]+', sentence)


def separa_palavras(phrase: str) -> list:
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da
    frase

    Args:
      phrase(str): A frase a ser dividida em palavras 
    
    Returns:
        list: Uma lista de strings onde cada string é uma palavra
    """
    return phrase.split()


def n_palavras_unicas(list_words: list) -> int:
    """Essa funcao recebe uma lista de palavras e devolve o
    numero de palavras que aparecem uma unica vez

    Args:
      list_words(list): 

    Returns:
        int: Número de palavras únicas em uma lista
    """
    freq = dict()
    uniq = 0
    for word in list_words:
        w = word.lower()
        if w in freq:
            if freq[w] == 1:
                uniq -= 1
            freq[w] += 1
        else:
            freq[w] = 1
            uniq += 1

    return uniq


def n_palavras_diferentes(list_words: list) -> int:
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas

    Args:
      list_words(list): 

    Returns:
        int: Número de palavras diferentes
    """
    freq = dict()
    for word in list_words:
        w = word.lower()
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return len(freq)


def compara_assinatura(main_sign: list, text_sign: list) -> float:
    """Essa funcao recebe duas assinaturas de texto e deve devolver o grau
    de similaridade entre as assinaturas.

    Args:
      main_sign: param text_sign:
      text_sign: 

    Returns:
        float: Grau de similaridade entre as assinaturas
    """
    sign_calc = 0
    for i, _ in enumerate(main_sign):
        sign_calc += abs(main_sign[i] - text_sign[i])
    
    return sign_calc / 6


def calcula_assinatura(text: str) -> list:
    """Essa funcao recebe um texto e devolve uma lista com a assinatura
    do texto.

    Args:
      text(str): Texto a ser avaliado

    Returns:
        list:
    """
    def avg_words(words):
        """Calcula a média """
        total_len = 0
        for word in words:
            total_len += len(word)

        return total_len / len(words)

    def type_token(words):
        """ """
        return n_palavras_diferentes(words) / len(words)

    def hapax_legomana(words):
        """ """
        return n_palavras_unicas(words) / len(words) 

    def avg_sentences(sentences):
        """ """
        carac_len = 0
        for sentence in sentences:
            carac_len += len(sentence)

        return carac_len / len(sentences)

    def complex_sentences(phrases, sentences):
        """ """
        return len(phrases) / len(sentences)

    def avg_phrases(phrases):
        """ """
        carac_len = 0
        for phrase in phrases:
            carac_len += len(phrase)

        return carac_len / len(phrases)


    sentences = separa_sentencas(text)

    phrases = []
    for sentence in sentences:
        phrases += separa_frases(sentence)

    words = []
    for phrase in phrases:
        words += separa_palavras(phrase)

    return [avg_words(words), type_token(words), hapax_legomana(words), avg_sentences(sentences), complex_sentences(phrases, sentences), avg_phrases(phrases)]


def avalia_textos(texts: list, main_sign: list) -> int:
    """Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.

    Args:
      texts(list): Textos a serem avaliados
      main_sign(list): Assinatura base

    Returns:
        int: Número do texto com maior prob de ter sido infectado
    """
    list_sign = []
    ans = float('inf')
    temp = []

    for text in texts:
        temp = []
        list_sign.append(calcula_assinatura(text))

    for i, text_sign in enumerate(list_sign):
        temp.append(compara_assinatura(main_sign, text_sign))
        if ans > temp[i]:
            ans = i
    
    return ans
    
    
def main() -> None:
    """ """
    print('\n\t\tSIMILARIDADE\n')
    print('Digite 1 para calcular a similaridade entre textos.')
    S = 1 - int(input('Digite 2 para calcular a assinatura de um texto: '))

    if S:
        txt = input('\nInsira o texto: ')
        ass = calcula_assinatura(txt)
        print(f'\nAssinatura do texto:\n')
        print(f'Tamanho medio das palavras: {ass[0]}')
        print(f'Relação Type-Token: {ass[1]}')
        print(f'Razão Hapax Legomana: {ass[2]}')
        print(f'Tamanho médio de sentença: {ass[3]}')
        print(f'Complexidade média da sentença: {ass[4]}')
        print(f'Tamanho medio de frase: {ass[5]}')
        return None
    
    main_sign = le_assinatura()
    texts = le_textos()

    ans = avalia_textos(texts, main_sign)

    print(f'O autor do texto {ans + 1} está infectado com COH-PIAH')


if __name__ == "__main__":
    main()