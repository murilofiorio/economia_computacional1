"""
Programa Soma
Descrição: este programa lê doi números inteiros digitados pelo usuário e põe na tela a soma deles.
Autor: Murilo Fiorio
Data: 12/04/2024
Versão: 0.0.1
"""

# Alocação de Memória

i: int = 0

numero: int = 0

soma: int = 0

# Entrada de Dados e Processamento de Dados

while i < 2:
    numero = int(input(f"Digite a parcela {i+1}:"))
    soma = soma + numero
    i += 1

# Saída de Dados

print(f"A soma dos números digitados é igual a {soma}.")