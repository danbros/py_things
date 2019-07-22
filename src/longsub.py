#!/usr/bin/env python3

# @author: danbros
# Pset1 do curso MITx: 6.00.1x (edX)

"""
Imprime a maior substring de uma string recebida ordenada alfabeticamente

Exemplo:
>>> s = 'azcbobobegghakl'
A maior substring or
"""

s = input('Entre com uma string: ')
s = 'azcbobobegghakl'

temp = sub_s = s[0]

for i, _ in enumerate(s[:-1]):

    if s[i] <= s[i+1]:
        temp += s[i+1]
        if len(temp) > len(sub_s):
            sub_s = temp
    else:
        temp = s[i+1]

print(sub_s)