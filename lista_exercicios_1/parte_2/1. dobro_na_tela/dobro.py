"""
"""

# Alocação de Memória

a: float = 0

# Entrada de Dados

a = float(input('Digite um número'))

# Processamento de Dados e Saída de Dados

if a < 10:
    dobro = a*2
    print(dobro)
elif 10 <= a <= 20:
    divide = a/2
    print(divide)
else:
    print("Número não válido.")