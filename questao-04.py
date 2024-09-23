# Dicionário com os valores de faturamento por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o total de faturamento
total_faturamento = sum(faturamento.values())

# Calcula e exibe o percentual de representação de cada estado
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
