def inverteString(string: str):
    stringInvertida = ''
    tamanhoStr = len(string)

    for i in range(tamanhoStr-1, -1, -1):
        stringInvertida += string[i]

    return stringInvertida

# Exemplo de uso
entrada = str(input("Digite uma string a ser invertida: "))
print(f'A string invertida é : {inverteString(entrada)}')