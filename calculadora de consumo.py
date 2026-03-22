# Entrada:
nome = input("Digite o nome do aparelho: ")
potencia = int(input("Digite a potência do aparelho em watts (W): "))
tempo_medio_consumo = float(input("Digite o tempo médio de consumo diario em horas: "))

# Processamento:
consumo_mensal = (potencia * tempo_medio_consumo * 30)/1000
custo_estimado = 0.75 * consumo_mensal

# Saída:
print(f"o consumo estimado é de: {consumo_mensal:.3f}, e o custo estimado é de: {custo_estimado:.3f}")