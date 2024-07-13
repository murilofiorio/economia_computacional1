"""
"""

# Alocação de Memória

intervalo: list = []
pares: list = []
extremidade_1: int = 0
extremidade_2: int = 0

# Entrada de Dado

extremidade_1 = int(input("Qual valor da primeira extremidade? "))
extremidade_2 = int(input("Qual valor da segunda extremidade? "))

# Processamento de Dados

for i in range(extremidade_1, extremidade_2 + 1):
    intervalo.append(i) # adiciona o "i" tal que o resto da divisão deste i contido no intervalo é 0

for i in intervalo:
    if i % 2 == 0:
        pares.append(i)

# Saída de Dados

print(pares)