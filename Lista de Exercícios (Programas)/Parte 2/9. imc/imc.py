"""
"""

# Alocação de Memória

ind_massa: float = 0
altura: float = 0
peso: float = 0

# Entrada de Dados

altura = float(input("Qual sua altura em metros? "))
peso = float(input('Qual seu peso em kg? '))

# Processamento e Saída de Dados

ind_massa = peso / altura**2

if ind_massa <= 18.5:
    print(f"Com índice IMC de {ind_massa:.2f}, você está excessivamente magro(a).")

elif 18.5 < ind_massa <= 25:
    print(f"Com índice IMC de {ind_massa:.2f}, você está com peso normal.")

elif 25 < ind_massa <= 30:
    print(f"Com índice IMC de {ind_massa:.2f}, você está com sobrepeso.")

elif ind_massa >= 30:
    print(f"Com índice IMC de {ind_massa:.2f}, você está obeso(a).")
else:
    print(f"Valores errados informados.")
