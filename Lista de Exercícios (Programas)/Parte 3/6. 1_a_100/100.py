"""
"""

# Alocação de Memória

intervalo: list = []
extremidade_esq: int = 0
extremidade_dir: int = 0

# Entrada de Dados

extremidade_esq = int(input("Digite a primeira extremidade: "))
extremidade_dir = int(input("Digite a segunda extremidade: "))

# Processamento de Dados

for i in range(extremidade_esq, extremidade_dir + 1):
    intervalo.append(i)

# Saída de Dados

print(intervalo)