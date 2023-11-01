def filtra(lista,n):
    lista1 = []
    for palavra in lista:
        if len(palavra) == n and (palavra[0].isnumeric() or palavra[0].isalnum()):
            if palavra.lower() not in lista1:
                lista1.append(palavra.lower())
    return lista1

import random

def inicializa(lista):
    dic = {}
    dic['n'] = len(lista[0])
    dic['tentativas'] = len(lista[0])+1
    dic['especuladas'] = []
    dic['sorteada'] = random.choice(lista)
    return dica