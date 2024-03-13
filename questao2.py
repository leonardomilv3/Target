def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def verifica_sequencia_fibonacci(numero):
    fibonacci = fibonacci_sequence(numero)
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci até {fibonacci[-1]}."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci até {fibonacci[-1]}."

# Exemplo de uso
numero_informado = int(input("Informe um número: "))
print(verifica_sequencia_fibonacci(numero_informado))
