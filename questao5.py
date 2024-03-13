def invertaString(string: str):
    stringInvertida = ''
    tamanhoStr = len(string)

    for i in range(tamanhoStr-1, -1, -1):
        stringInvertida += string[i]

    return stringInvertida


print(invertaString('abcdefg'))

print(invertaString('arroz com feijão'))

print(invertaString('batata frita'))
