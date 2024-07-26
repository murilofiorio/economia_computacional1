"""
Programa Produto
Descrição: este programa, usando programação funcional, recebe dois valores e retorna o produto entre eles
Autor: Murilo Fiorio
Data: 25/07/2024
Versão: 1.0.0
"""

def entrada() -> tuple[float, float]:
    x = float(input("Digite x: "))
    y = float(input("Digite y: "))
    return x, y

def calcula_produto(x: float, y: float) -> float:
    produto = x * y
    return produto

def saida(produto: float) -> float:
    print(produto)

def main():
    x, y = entrada()
    produto = calcula_produto(x, y)
    print(produto)

if __name__ == "__main__":
    main()