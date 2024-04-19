"""
"""

# Alocação de Memória

principal: float = 0
prazo: int = 0
taxa_juros: int = 0
capitalizacao: int = 0

# Entrada de Dados

prazo = float(input('Prazo em anos:'))
principal = float(input('Valor inicial: '))
taxa_juros = float(input('Taxa de juros anual (%): '))

# Processamento de Dados

taxa_juros = taxa_juros/100

capitalizacao = principal*(1 + taxa_juros*prazo)

# Saída de Dados

print(f"O valor capiralizado após {prazo} anos sob a taxa de {taxa_juros*100}% é de R${capitalizacao:0.2f}.")
