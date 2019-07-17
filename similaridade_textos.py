import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e
    devolve uma assinatura a ser comparada com os textos fornecidos'''

    print("\nBem-vindo ao detector automático de COH-PIAH.\n\n")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    texts = []
    text = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")
    while text:
        texts.append(text)
        i += 1
        text = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")

    return texts


def separa_sentencas(text):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentences = re.split(r'[.!?]+', text)
    if sentences[-1] == '':
        del sentences[-1]
    return sentences


def separa_frases(sentence):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentence)


def separa_palavras(phrase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return phrase.split()


def n_palavras_unicas(list_words):
    '''Essa funcao recebe uma lista de palavras e devolve o
    numero de palavras que aparecem uma unica vez'''
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


def n_palavras_diferentes(list_words):
    '''Essa funcao recebe uma lista de palavras e devolve o
    numero de palavras diferentes utilizadas'''
    freq = dict()
    for word in list_words:
        w = word.lower()
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return len(freq)


def compara_assinatura(main_sign, text_sign):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto
    e deve devolver o grau de similaridade nas assinaturas.'''
    sign_calc = 0
    for i, _ in enumerate(main_sign):
        sign_calc += abs(main_sign[i] - text_sign[i])
    
    return sign_calc / 6


def calcula_assinatura(text):
    '''Essa funcao recebe um texto e devolve uma lista com 
    a assinatura do texto.'''
    def avg_words(words):
        total_len = 0
        for word in words:
            total_len += len(word)

        return total_len / len(words)

    def type_token(words):
        return n_palavras_diferentes(words) / len(words)

    def hapax_legomana(words):
        return n_palavras_unicas(words) / len(words) 

    def avg_sentences(sentences):
        carac_len = 0
        for sentence in sentences:
            carac_len += len(sentence)

        return carac_len / len(sentences)

    def complex_sentences(phrases, sentences):
        return len(phrases) / len(sentences)

    def avg_phrases(phrases):
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


def avalia_textos(texts, main_sign):
    '''Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
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
    
    
def main():
    main_sign = le_assinatura()
    texts = le_textos()

    ans = avalia_textos(texts, main_sign)

    print(f'O autor do texto {ans + 1} está infectado com COH-PIAH')
    

main()