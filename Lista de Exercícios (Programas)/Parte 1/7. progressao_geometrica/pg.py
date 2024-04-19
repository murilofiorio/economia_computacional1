"""

"""

# Alocação de Memória

a_1: float = 0
q: float = 0
n: int = 0
a_n: float = 0
s_n: float = 0
s_inf: float = 0

# Entrada de Dados

a_1: float = float(input('Digite o primeiro termo: '))
q: float = float(input('Digite a razão: '))
n: int = int(input('Digite a quantidade de termos: '))

# Processamento de Dados

a_n: float = a_1*(q**(n - 1))
s_n: float = (a_1*((q**n)-1))//(q - 1)
s_inf: float = a_1//(1 - q)

# Saída de Dados

print(f"O termo da posição {n} é {a_n}.\nA soma de {n} termo é {s_n}.\nA soma de infinitos termos é {s_inf}.")