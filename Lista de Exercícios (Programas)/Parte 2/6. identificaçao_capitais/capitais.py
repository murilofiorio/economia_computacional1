"""
"""

# Alocação de Memória

capitais = ['Porto Alegre', 'Florianópolis', 'Curitiba']

x: str = 0

# Entrada de Dados

x = input('Digite uma capital: ')

# Processamento e Saída de Dados

if x in capitais:
    print("É uma capital de um Estado da região sul do Brasil.")

else:
    print("Não é uma capital presente na região sul do Brasil.")