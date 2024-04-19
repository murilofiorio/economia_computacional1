"""


"""

# Alocação de Memória

salario_bruto: float = 0
salario_liquido: float = 0
horas_trabalhadas: float = 0
total_desconto: float = 0
imposto: float = 0.3
valor_hora: int = 40

# Entrada de Dados

horas_trabalhadas: float = float(input('Qual o número de horas trabalhadas?'))

# Processamento de Dados

salario_bruto: float = horas_trabalhadas*valor_hora
total_desconto: float = salario_bruto*imposto
salario_liquido: float = salario_bruto - total_desconto

# Saída de Dados

print(f"Salário bruto no valor de R$ {salario_bruto:.2f}.\nTotal de desconto no valor de RS {total_desconto:.2f}.\nSalário líquido no valor de R$ {salario_liquido:.2f}.")