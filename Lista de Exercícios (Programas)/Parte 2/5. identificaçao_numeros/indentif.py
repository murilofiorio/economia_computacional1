"""
"""

# Alocação de Memória

a: float = 0

# Entrata de Dados

a = float(input('Digite um número: '))

# Processamento de Saída de Dados

if a < 0:
    print(f"{a} é um número negativo.")
elif a == 0:
    print(f"{a:.0f} é um número nulo.")
else:
    print(f"{a} é um número positivo.")