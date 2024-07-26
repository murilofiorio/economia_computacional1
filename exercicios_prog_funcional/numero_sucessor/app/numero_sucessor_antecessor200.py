"""
Programa Número Sucessor e Antecessor
Descrição: este programa recebe um valor numérico e retorna ou seu valor sucessor, ou seu valor antecessor utilizando o paradigma da programação funcional
Autor: Murilo Fiorio
Data: 25/07/2024
Versão: 2.0.0
"""

def entrada() -> tuple[str, float]:
    operacao = input("Digite 'a' para antecessor e 's' para sucessor: ")
    numero = int(input("Digite um número inteiro: "))
    return operacao, numero

def processamento(operacao: str, numero:int) -> float:
    if operacao == "a":
        antecessor = numero -1
        return antecessor
    elif operacao == "s":
        sucessor = numero + 1
        return sucessor
    else:
        print("Você não digitou 'a' nem 'b'.")

def saida(resultado) -> float:
    print(resultado)

def main() -> None:
    operacao, numero = entrada()
    resultado = processamento(operacao, numero)
    saida(resultado)

if __name__ == "__main__":
    main()