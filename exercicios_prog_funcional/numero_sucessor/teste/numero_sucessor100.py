"""
Programa Número Sucessor
Descrição: este programa recebe um valor numérico e retorna seu valor sucessor utilizando o paradigma da programação funcional
Autor: Murilo Fiorio
Data: 25/07/2024
Versão: 1.0.0
"""

def entrada() -> float:
    numero = int(input("Digite um número inteiro: "))
    return numero

def processamento(x:int) -> int:
    sucessor = x + 1
    return sucessor

def saida(sucessor) -> float:
    print(sucessor)

def main() -> None:
    numero = entrada()
    sucessor = processamento(numero)
    saida(sucessor)

if __name__ == "__main__":
    main()