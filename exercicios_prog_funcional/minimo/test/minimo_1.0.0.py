"""
Programa Mínimo
Descrição: este programa, usando programação funcional, recebe dois números e imprimi o menor deles
Autor: Murilo Fiorio
Data: 25/07/2024
Versão: 1.0.0
"""

def entrada() -> tuple[float, float]:
    a = float(input("Digite o primeiro número real: "))
    b = float(input("Digite o segundo número real: "))
    return a, b

def saida_min(a: float, b: float) -> float:
    if a < b:
        return a
    elif a > b:
        return b
    else:
        print(f"{a}={b}")

def main() -> None:
    a, b = entrada()
    min = saida_min(a, b)
    print(min)

if __name__ == "__main__":
    main()