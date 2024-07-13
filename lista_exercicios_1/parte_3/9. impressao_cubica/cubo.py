"""
"""

# Alocação de Memória

numeros: list = []
quadrados: list = []
numero: float = 0
quantidade: int = 0
resultado: float = 0

# Entrada de Dados

quantidade = int(input("Qual a quantidade de números que deseja imprimir seus quadrados? "))

for i in range(1, quantidade + 1): # cria intervalo de (1, n+1)
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)
    numero = 0

# Processamento de Dados

quadrados = [x**3 for x in numeros]

# Processamento de Dados

quadrados = [x**3 for x in numeros]

# Saída de Dados

print(quadrados)