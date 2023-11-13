from colorama import init, Fore
import random
import colorama


colorama.init()

print(f' ===========================\n|                           |\n| Bem-vindo ao Insper Termo |\n|                           |\n ==== Design de Software === \n\nComandos: desisto\n\n Regras:\n\n  - Você tem {Fore.RED}6{Fore.RESET} tentativas para acertar uma palavra aleatória de 5 letras.\n  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n    . {Fore.BLUE}Azul{Fore.RESET}   : a letra está na posição correta;\n    . {Fore.YELLOW}Amarelo{Fore.RESET}: a palavra tem a letra, mas está na posição errada;\n    . Branco : a palavra não tem a letra.\n  - Os acentos são ignorados;\n  - As palavras podem possuir letras repetidas.\n\nSorteando uma palavra...\nJá tenho uma palavra! Tente adivinhá-la!\n\nVocê tem 6 tentaviva(s)')


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
filt = filtra(lista_palavras, n)


j = 1
dic = inicializa(filt)


d = ' --- --- --- --- ---'
l1 = '|   |   |   |   |   |'
l2 = '|   |   |   |   |   |'
l3 = '|   |   |   |   |   |'
l4 = '|   |   |   |   |   |'
l5 = '|   |   |   |   |   |'
l6 = '|   |   |   |   |   |'


lin = [d, l1, l2, l3, l4, l5, l6]


continua = True


while continua:
    sorteada = dic['sorteada']
    spec = str(input('Qual o seu palpite? '))


    if spec == 'desisto':
        if input('Tem certeza que deseja desistir? [s/n] ') == 's':
            print(f'>>> A palavra era: {sorteada}\n')
            p = str(input('Deseja jogar novamente? [s/n] '))


            if p == 's':
                filt = filtra(lista_palavras, n)
                dic = inicializa(filt)
                j = 0
            else:
                print('\n\n\nAté mais!')
                continua = False
    elif len(spec) != 5:
        print("São permitidas apenas palavras de 5 caractéres.")
    elif spec not in filt:
        print('Palavra inexistente')
    elif spec not in dic['especuladas']:
        j += 1
        dic['especuladas'].append(spec)
        resta = len(filt[0]) + 1 - j
        tentativa = indica_posicao(sorteada, spec)
        acerto = tentativa.count(0)


        for i in range(len(lin)):
            if i == j:
                nova = '| '
            for x in range(len(tentativa)):
                if tentativa[x] == 0:
                    nova += Fore.RED + f'{spec[x]}' + Fore.RESET + ' | '
                else:
                    nova += f'{spec[x]}' + ' | '
            lin[i] = nova
            if i != 0:
                print(lin[i])
            print(d)
           
            if acerto == 5:
                print(f'\n*** Parabéns! Você acertou após {j} tentativa(s)')
                j = 0
            else:
                print(f'\nVocê tem {resta} tentativa(s)')
    else:
        print('Palavra já testada!')


colorama.deinit()
