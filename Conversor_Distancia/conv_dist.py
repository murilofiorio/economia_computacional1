"""
Program conv_dist

Descrição: este programa lê um valor em metros e o converta para milímetros.
Autor: Murilo Fiorio
Data: 12/04/2024
Versão: 0.0.1

"""

# Alocação de Memória

metros: float = 0

milimetros: float = 0

## Entrada de Dados

metros = float(input("Digite a distância em metros:"))

# Processamento de Dados

milimetros = 1000*metros

# Saída de Dados

print(f"\nA distância em milímetros é igual a {milimetros}")