"""
"""

# Alocação de Memória

exp_ret: float = 0
r_f: float = 0
r_m: float = 0
b_i: float = 0

# Entrada de Dados

r_f: float = float(input('Retorno do Ativo sem Risco: '))
r_m: float = float(input('Retorno da Carteira de Mercado: '))
b_i: float = float(input('Coeficiente de Sensibilidade: '))

# Processamento de Dados

exp_ret = r_f + b_i*((r_m - r_f))

# Saída de Dados

print(f"O retorno esperado para a empresa é {exp_ret}.")