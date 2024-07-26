"""
Programa Mínimo-Máximo
Descrição: este programa, usando programação funcional, recebe dois números reais e imprimi o menor ou o maior deles a depender da solicitação
Autor: Murilo Fiorio
Data: 25/07/2024
Versão: 2.0.0
Mudança: função máximo acrescentada
"""

def entrada() -> tuple[str, float, float]:
    operacao = input("'m' para mínimo e 'M' para máximo: ")
    a = float(input("Digite o primeiro número real: "))
    b = float(input("Digite o segundo número real: "))
    return operacao, a, b

def calculo_min_max(operacao: str, a: float, b: float) -> float:
    if operacao == "m" and a < b:
        return a
    elif operacao == "m" and a > b:
        return b
    elif operacao == "M" and a < b:
        return b
    elif operacao == "M" and a > b:
        return a
    elif a == b:
        raise ValueError(f"{a}={b}.")
    else:
        raise ValueError(f"'{operacao}' não válida.")

def main() -> None:
    try:
        operacao, a, b = entrada()
        min_max = calculo_min_max(operacao, a, b)
        print(min_max)
    except ValueError as e:
        print(f"{e}")

if __name__ == "__main__":
    main()