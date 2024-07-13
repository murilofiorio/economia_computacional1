"""
"""

# Alocação de Memória

num1: float = 0
num2: float = 0
num3: float = 0

# Entrada de Dados

num1: float = float(input('1º número:'))
num2: float = float(input('2º número:'))
num3: float = float(input('3º número:'))

# Processamento de Dados

"""
ex: 1º número = 7; 2º número = 9; 3º número = 7,5
então: 7 > 9 = False, portanto 1º número = 7 e 2º número = 9
       9 > 7,5 = True, portanto 2º número = 7,5 e 3º número = 9
       7 > 9 = False, portanto 1º número = 7 e 3º número = 9

       1º número = 7, 2º número = 7,5 e 3º número = 9
"""

if num1 > num2:
    num1, num2 = num2, num1 # associa num1 = num2, pois menor para o maior
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num3:
    num1, num3 = num3, num1

# Saída de Dados

print(f"Os números em ordem crescente são: {num1}, {num2}, {num3}.")