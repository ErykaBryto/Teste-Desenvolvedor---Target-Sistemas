def fibonacci(n):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1

    # Verifica se o número informado é 0 ou 1, que são parte da sequência
    if n == 0 or n == 1:
        return True

    # Calcula a sequência até que o número 'b' seja maior ou igual a 'n'
    while b < n:
        a, b = b, a + b

    # Retorna True se o número for encontrado na sequência
    return b == n

# Função para verificar se o número informado pertence à sequência
def verificar_fibonacci(num):
    if fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

# Exemplo de uso
num_informado = int(input("Informe um número: "))
verificar_fibonacci(num_informado)
