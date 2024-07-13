"""
"""

# Alocação de Memória

a: float = 0
b: float = 0
x: float = 0
c: float = 0
r_1: float = 0
r_2: float = 0
x_v: float = 0 # x do vértice
y_v: float = 0 # y do vértice
resultado: float = 0

# Entrada de Dados

a: float = float(input('Digite o coeficiente angular de a*x^2: '))
b: float = float(input('Digite o coeficiente angular de b*x: '))
c: float = float(input('Digite o coeficiente linear c: '))
x: float = float(input('Digite a variável x: '))

# Processamento de Dados

r_1 = (-b - ((b**2 - 4*a*c)**(1/2))) / (2*a)
r_2 = (-b + ((b**2 - 4*a*c)**(1/2))) / (2*a)
x_v = (-b)/(2*a)
y_v = -((b**2 - 4*a*c)/ (4*a))
resultado = a*x**2+b*x+c

# Saída de Dados

print(f"\n1ª raiz: {r_1:0.2f};\n2ª raiz: {r_2:0.2f}.\n\nPonto máximo\mínimo da função: ({x_v:0.2f}, {y_v:0.2f}).\n\nResultao de f({x})= {a}{x}^2 + {b}{x} + {c} = {resultado:0.2f}\n")