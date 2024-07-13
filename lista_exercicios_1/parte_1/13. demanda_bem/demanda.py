"""
"""

# Alocação na Memória

preco: float = 0
renda: float = 0
q: float = 0

# Entrada de Dados

renda = float(input('Qual sua renda? '))
preco = float(input('Qual o preço do bem? '))

# Processamento de Dados

q = renda/preco

# Saída de Dados

print(f"A demanda total pelo único bem em questão dada por um único consumidor é de {q:.2f} quantidades.")
