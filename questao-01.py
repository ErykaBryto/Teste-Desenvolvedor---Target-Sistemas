def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K

    return SOMA

# Executa o programa e imprime o resultado
resultado = calcular_soma()
print("O valor final de SOMA é:", resultado)
