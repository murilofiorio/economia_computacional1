"""
"""

# Alocação de Memória



x: float = 0
y: float = 0
z: float = 0
media: float = 0

# Entrada de Dados

x: float = float(input("1ª nota (de 0 a 10): "))
y: float = float(input("2ª nota (de 0 a 10): "))
z: float = float(input("3ª nota (de 0 a 10): "))

# Processamento e Saída de Dados

media = (x + y + z)/ 3

if 0 < media < 5:
    print(f"Com média {media}, o aluno está reprovado.")
elif 5 <= media < 6:
    print(f"Com média {media}, o aluno está em recuperação.")
elif 6 < media <= 10:
    print(f"Com média {media}, o aluno está aprovado.")
else:
    print(f"Números para a média informados errados.")