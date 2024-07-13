"""
"""

# Alocação de Memória

extremidade_1: int = 0
extremidade_2: int = 0
soma: int = 0

# Entrada de Dados

extremidade_1: int = int(input("1ª Extremidade: "))
extremidade_2: int = int(input("2ª Extremidade: "))

# Processamento de Dados

soma = sum(range(extremidade_1, extremidade_2 +1))

# Saída de Dados

print(soma)