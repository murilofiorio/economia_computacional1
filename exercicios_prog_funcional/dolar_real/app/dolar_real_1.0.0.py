"""
Programa Dólar-Real
Descrição: este programa, usando paradigma funcional, recebe uma quantidade em real e a cotação do dólar e retorna a quantidade de dólar equivalente a quantidade de real recebida
Autor: Murilo Fiorio
Data: 25/07/2024
Versão: 1.0.0
"""

def entrada() -> tuple[float, float]:
    real = float(input("Digite a quantidade em reais: "))
    cotacao = float(input("Digite a cotação do dólar: "))
    return real, cotacao

def calcula_dolar(real: float, cotacao: float) -> float:
    dolar = real * cotacao
    return dolar

def saida(dolar: float) -> None:
    print(dolar)

def main() -> None:
    real, cotacao = entrada()
    dolar = calcula_dolar(real, cotacao)
    print(dolar)

if __name__ == "__main__":
    main()