"""
"""

# Alocação de Memória

a: float = 0
x_n: float = 0
raiz: float = 0

# Entrada de Dados

a = float(input('Digite o número a ser calculado sua raiz quadrada: '))
x_n = float(input(f"Digite uma estimativa iterativa para a raiz quadrada de {a}: "))

# Processamento de Dados

if a < 0:
    print("Não existe raiz real de número negativos.")

else :
    raiz = 1/2*(x_n + a / x_n)

# Saída de Dados

print(f"Raiz quadrada aproximada de {a} igual a {raiz}")