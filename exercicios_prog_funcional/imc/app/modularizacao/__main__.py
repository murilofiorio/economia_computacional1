from entrada import entrada
from calcula_imc import calcula_imc
from saida import saida

def main():
    altura, peso = entrada()
    imc = calcula_imc(altura, peso)
    print(f"{imc:.2f}")

if __name__ == "__main__":
    main()