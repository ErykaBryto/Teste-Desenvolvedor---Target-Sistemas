import json

# Função para carregar dados de faturamento a partir do arquivo 'dados.json'
def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados

# Função para calcular o menor, maior e dias acima da média
def analisar_faturamento(dados):
    # Filtra os dias com faturamento maior que zero
    faturamentos = [dia['valor'] for dia in dados if 'valor' in dia and dia['valor'] > 0]
    
    # Calcula o menor e maior faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    
    # Calcula a média do faturamento
    media_faturamento = sum(faturamentos) / len(faturamentos)
    
    # Conta os dias em que o faturamento foi maior que a média
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_faturamento)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Função principal
def main():
    # Carregar dados do arquivo 'dados.json'
    arquivo_json = 'dados.json'
    dados_faturamento = carregar_faturamento(arquivo_json)
    
    # Analisar os dados de faturamento
    menor, maior, dias_acima_media = analisar_faturamento(dados_faturamento)
    
    # Exibir resultados
    print(f"Menor faturamento: {menor}")
    print(f"Maior faturamento: {maior}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Executa o programa
if __name__ == "__main__":
    main()
