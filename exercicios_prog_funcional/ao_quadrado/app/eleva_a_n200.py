"""
Programa Calcula Quadrado
Descrição: este programa recebe dois valroes x e y e retorna o quadrado da soma destes utilizando programação funcional
Autor: Murilo Fiorio
Data: hoje
Versão: 1.0.0
"""

def entrada() -> tuple[int, float, float]:
    expoente = int(input("Digite o número do expoente: "))
    x = float(input("Digite o número x: "))
    y = float(input("Digite o número y: "))
    return expoente, x, y

def calcula_exponencial(expoente: int, x: float, y: float) -> float:
    exponencial = (x + y)**expoente
    return exponencial

def saida(exponencial: float) -> float:
    print(exponencial)

def main() -> None:
    expoente, x, y = entrada()
    resultado = calcula_exponencial(expoente, x, y)
    saida(resultado)

if __name__ == "__main__":
    main()