from lista import lista_palavras
import random
from colorama import init, Fore, Back, Style
import colorama


colorama.init()

n = 5
filtrada = []

print(f' ===========================\n|                           |\n| Bem-vindo ao Insper Termo |\n|                           |\n ==== Design de Software === \n\nComandos: desisto\n\n Regras:\n\n  - Você tem {Fore.BLUE}6{Fore.RESET} tentativas para acertar uma palavra aleatória de 5 letras.\n  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n    . {Fore.BLUE}Azul{Fore.RESET}   : a letra está na posição correta;\n    . {Fore.YELLOW}Amarelo{Fore.RESET}: a palavra tem a letra, mas está na posição errada;\n    . Branco : a palavra não tem a letra.\n  - Os acentos são ignorados;\n  - As palavras podem possuir letras repetidas.\n\nSorteando uma palavra...\nJá tenho uma palavra! Tente adivinhá-la!\n\nVocê tem 6 tentaviva(s)')

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

def inidica_posicao(sorteada,string):
    i = 0
    lista1 = []
    if len(sorteada) != len(string):
        return []
    while i < len(string):
        if string[i] == sorteada[i]:
            lista1.append(0)
        elif string[i] in sorteada:
            lista1.append(1)
        elif string[i] not in sorteada:
            lista1.append(2)
        i += 1
    return lista1

for palavra in lista_palavras:
    palavra = palavra.lower() 
    palavra = palavra.strip("!?,.@")  
    if len(palavra) == n and palavra not in filtrada:
        filtrada.append(palavra)

j=1

dicio = {'n': len(filtrada[0]),  'tentativas': len(filtrada[0]) + 1, 'especuladas': [],  'sorteada': random.choice(filtrada)}

d = ' --- --- --- --- ---'
linha1 ='|   |   |   |   |   |'
linha2 ='|   |   |   |   |   |'
linha3 ='|   |   |   |   |   |'
linha4 ='|   |   |   |   |   |'
linha5 ='|   |   |   |   |   |'
linha6 ='|   |   |   |   |   |'

linha = [d, linha1, linha2, linha3, linha4, linha5, linha6]

jog = 0
while continua:
    sorteada = dic['sorteada']

    especulada = str(input('Qual é seu palpite? '))
    if especulada == 'desisto':
        if input('Tem certeza que deseja desistir da rodada? [s|n] ') == 's':
            print(f'>>> Que deselegante desistir, a palavra era: {sorteada}\n')
            p = str(input('Jogar novamente? [s|n] '))
            if p == 's':
                dic = {'n': len(filtrada[0]),  'tentativas': len(filtrada[0]) + 1, 'especuladas': [],  'sorteada': random.choice(filtrada)}
                jog = 0
            else:
                print('\n\n\nAté a próxima!')
                continua = 0
    elif len(especulada) != 5:
        print("apenas palavras de 5 letras")
    elif especulada not in filtrada:
        print('palavra desconhecida')
    elif especulada not in dicio['especuladas']:
        j += 1
        dic['especuladas'].append(especulada)
        resta = int(len(filtrada[0]) + 1) - jog
        tentativa = inidica_posicao(sorteada, especulada)
        acerto = 0
        for i in tentativa:
            if i == 0:
                acerto += 1
        else:
            if resta == 0:
                print('Perdeu')
                pergunta = str(input('Jogar novamente? [s|n] '))
                if p == 's':
                    dic = {'n': len(filtrada[0]),  'tentativas': len(filtrada[0]) + 1, 'especuladas': [],  'sorteada': random.choice(filtradas)}
                    j = 0
else:
                    j = 0
            print('\nInsper :: TERMO\n')
    
    for i in range (len(linha)):
        if i == jog:
            nova = '| '
        for x in range (len(tentativa)):
             if tentativa[x] == 0:
                nova += Fore.RED + f'{especulada[x]}' + Fore.RESET+ ' | '
    else:
        nova += f'{especulada[j]}' + ' | '
        linha[i] = nova
        if i != 0:
            print(linha[i])
        print(d)
        if acerto == 5:
            print(f'\n*** Parabéns! Você acertou após {jogadas} tentativa(s)')
            j = 0
        else:
            print(f'\nVocê tem {resto} tentativa (s)')
    elif:
        print('Palavra já testada!')
    colorama.deinit()

