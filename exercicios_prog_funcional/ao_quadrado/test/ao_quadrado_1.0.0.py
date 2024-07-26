"""
Programa Calcula Quadrado
Descrição: este programa recebe dois valroes x e y e retorna o quadrado da soma destes utilizando programação funcional
Autor: Murilo Fiorio
Data: hoje
Versão: 1.0.0
"""

def entrada() -> tuple[float, float]:
    x = float(input("Digite o número x: "))
    y = float(input("Digite o número y: "))
    return x, y

def calcula_quadrado(x: float, y: float) -> float:
    quadrado = (x + y)**2
    return quadrado

def saida(quadrado: float) -> float:
    print(quadrado)

def main() -> None:
    x, y = entrada()
    quadrado = calcula_quadrado(x, y)
    saida(quadrado)

if __name__ == "__main__":
    main()