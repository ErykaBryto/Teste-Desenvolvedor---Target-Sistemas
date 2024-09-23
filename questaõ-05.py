# Função para inverter uma string
def inverter_string(s):
    # Cria uma lista para armazenar os caracteres invertidos
    string_invertida = []
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida.append(s[i])
    
    # Converte a lista de caracteres de volta para uma string
    return ''.join(string_invertida)

# Exemplo de uso
entrada = input("Digite a string a ser invertida: ")
# Ou você pode definir uma string diretamente, por exemplo:
# entrada = "Hello, World!"

resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
