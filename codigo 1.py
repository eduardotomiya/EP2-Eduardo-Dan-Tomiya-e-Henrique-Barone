def filtra(lista,n):
    lista1 = []
    for palavra in lista:
        if len(palavra) == n and (palavra[0].isnumeric() or palavra[0].isalnum()):
            if palavra.lower() not in lista1:
                lista1.append(palavra.lower())
    return lista1