"""
"""

# Alocação de Memória

coeficientes: list = []
coeficiente: float = 0
grau: int = 0
resultado: float = 0
x: float = 0

# Entrada de Dados

grau: int = int(input('Digite o grau no polinômio: '))

"""
'range' cria um intervalo (tupla) de 0 até n; "+ 1" pois, como python começa a contar do 0,
se, p. ex., informado cinco, a range seria (0, 4), pois dentro deste intervalo, contém 5 elementos.
Ou seja, seria grau a menos do que o informando.
"""

for i in range(grau + 1): 
    coeficiente = float(input(f"Digite o coeficiente a_{i} de a_{i}*x^{i}: "))
    coeficientes.append(coeficiente)

x = float(input("Digite o valor de x: "))

# Processamento de Dados

"""
Em "coeficientes[i], ele chamará o coeficientes a_i colocado pelo usuário na posição i e
passará ao próximo.
"""


for i in range(grau + 1):
    resultado = resultado + coeficientes[i] * (x**i) # chama o coeficiente i e multiplica por x^i e soma com o resultado, que, quando i=0, portanto, resultado igual a zero, porém vai se acumulando

# Saída de Dados

print(f"O resultado é {resultado:.2f}")