"""
Programa Calcula IMC
Descrição: este programa, usando programação funcional, recebe peso e altura e retorna o imc
Autor: Murilo Fiorio
Data: 25/07/2024
Versão: 1.0.0
"""

def entrada() -> tuple[float, float]:
    altura = float(input("Digite a altura em metros: "))
    peso = float(input("Digite o peso em kg: "))
    return altura, peso

def calcula_imc(altura: float, peso: float) -> float:
    imc = peso / altura**2
    return imc

def saida(imc: float) -> float:
    print(imc)

def main():
    altura, peso = entrada()
    imc = calcula_imc(altura, peso)
    print(f"{imc:.2f}")

if __name__ == "__main__":
    main()