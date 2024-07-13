"""
"""


# Alocação de Memória

termos: list = []
a_i: float = 0 # cada termo que entrará na lista
r: float = 0 #razão
n: int = 0 # número de termos
a_1: float = 0 # primeiro termo

# Entrada de Dados

n: int = int(input('Qual o número de termos?'))
r: float = float(input('Qual a razão?'))
a_1 = float(input("Qual o primeiro termo? "))

# Processamento de Dados

for i in range(1, n + 1): # se começasse em 0, então daria errado a fórmula
    a_i = a_1 + (i - 1)*r
    termos.append(a_i)

# Saída de Dados

print(termos)