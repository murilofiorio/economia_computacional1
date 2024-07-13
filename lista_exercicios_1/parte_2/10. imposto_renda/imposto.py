# Alocação de Memória

salario: float = 0
horas: float = 0
imposto: float = 0

# Entrada de Dados

horas = float(input("Quantidade de horas trabalhadas: "))

# Processamento e Saída de Dados


salario = 20*horas

if salario <= 1000:
    imposto = salario*0
    salario = salario - imposto
    print(f" Salário líquido no valor de R${salario:.2f}.")

elif 1000 < salario <= 2500:
    imposto = salario_*0.1
    salario = salario - imposto
    print(f" Salário líquido no valor de R${salario:.2f}.")

elif 2500 < salario <= 5000:
    imposto = salario*0.2
    salario = salario - imposto
    print(f" Salário líquido no valor de R${salario:.2f}.")

elif salario >= 5000:
    imposto = salario*0.35
    salario = salario - imposto
    print(f" Salário líquido no valor de R${salario:.2f}.")

else :
    print("Valores errados informados.")