"""
"""

# Alocação de Memória

idade: int = 0
nome: str = 0

# Entrada de Dados

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))

# Processamento e Saída de Dados

if 0 <= idade < 18:
    print(f"{nome} não pode assistir a este filme.")

elif 18 <= idade <=100:
    print(f"{nome} pode assistir a este filme.")

else:
    print(f"{nome} está realmente vivo?")