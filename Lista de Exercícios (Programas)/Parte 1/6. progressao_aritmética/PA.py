"""

"""

# Alocação de Memória

r: float = 0 #razão
n: int = 0 # número de termos
a_1: float = 0 # primeiro termo
a_n: float = 0 # n-ésimo termo
s_n: float = 0 # soma de n-ésimos termos

# Entrada de Dados

a_1: float = float(input('Qual o primeiro termo?'))
n: int = int(input('Qual o número de termos?'))
r: float = float(input('Qual a razão?'))

# Processamento de Dados

a_n: float = a_1 + (n - 1)*r
s_n: float = ((a_1 + a_n)//2)*n

# Saída de Dados

print(f"O termo contido na {n}ª posição é {a_n}.\nA soma dos {n} termos é {s_n}")