from lista import lista_palavras
from colorama import init, Fore
import random
import colorama

colorama.init()

def filtra(lista, n):
    lista1 = []
    for palavra in lista:
        if len(palavra) == n and (palavra[0].isnumeric() or palavra[0].isalnum()):
            if palavra.lower() not in lista1:
                lista1.append(palavra.lower())
    return lista1

def inicializa(lista):
    dic = {}
    dic['n'] = len(lista[0])
    dic['tentativas'] = len(lista[0]) + 1
    dic['especuladas'] = []
    dic['sorteada'] = random.choice(lista)
    return dic

def indica_posicao(sorteada, string):
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

n = 5
filtrada = filtra(lista_palavras, n)


j = 1
dic = inicializa(filtrada)

d = ' --- --- --- --- ---'
linha1 = '|   |   |   |   |   |'
linha2 = '|   |   |   |   |   |'
linha3 = '|   |   |   |   |   |'
linha4 = '|   |   |   |   |   |'
linha5 = '|   |   |   |   |   |'
linha6 = '|   |   |   |   |   |'

linha = [d, linha1, linha2, linha3, linha4, linha5, linha6]

continua = True

while continua:
    sorteada = dic['sorteada']
    especulada = str(input('Qual é seu palpite? '))

    if especulada == 'desisto':
        if input('Tem certeza que deseja desistir da rodada? [s|n] ') == 's':
            print(f'>>> Que deselegante desistir, a palavra era: {sorteada}\n')
            p = str(input('Jogar novamente? [s|n] '))

            if p == 's':
                filtrada = filtra(lista_palavras, n)
                dic = inicializa(filtrada)
                j = 0
            else:
                print('\n\n\nAté a próxima!')
                continua = False
    elif len(especulada) != 5:
        print("Apenas palavras de 5 letras são permitidas.")
    elif especulada not in filtrada:
        print('Palavra desconhecida')
    elif especulada not in dic['especuladas']:
        j += 1
        dic['especuladas'].append(especulada)
        resta = len(filtrada[0]) + 1 - j
        tentativa = indica_posicao(sorteada, especulada)
        acerto = tentativa.count(0)

        for i in range(len(linha)):
            if i == j:
                nova = '| '
            for x in range(len(tentativa)):
                if tentativa[x] == 0:
                    nova += Fore.RED + f'{especulada[x]}' + Fore.RESET + ' | '
                else:
                    nova += f'{especulada[x]}' + ' | '
            linha[i] = nova
            if i != 0:
                print(linha[i])
            print(d)
            
            if acerto == 5:
                print(f'\n*** Parabéns! Você acertou após {j} tentativa(s)')
                j = 0
            else:
                print(f'\nVocê tem {resta} tentativa(s)')
    else:
        print('Palavra já testada!')

colorama.deinit()