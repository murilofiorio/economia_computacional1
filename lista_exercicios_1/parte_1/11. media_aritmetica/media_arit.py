"""
"""

# Alocação de Memória

a: float = 0
b: float = 0
c: float = 0
d: float = 0
media: float = 0

# Entrada de Dados

a: float = float(input('Digite o primeiro número: '))
b: float = float(input('Digite o segundo número: '))
c: float = float(input('Digite o terceiro número: '))
d: float = float(input('Digite o quarto número: '))

# Processamento de Dados

media = (a + b + c + d)/4

# Saída de Dados

print(f"A média de {a}, {b}, {c} e {d} é igual a {media}.")