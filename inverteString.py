def inverteString(string: str):
    stringInvertida = ''
    tamanhoStr = len(string)

    for i in range(tamanhoStr-1, -1, -1):
        stringInvertida += string[i]

    return stringInvertida

