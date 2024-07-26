from entrada import entrada
from calcula_dolar import calcula_dolar
from saida import saida

def main() -> None:
    real, cotacao = entrada()
    dolar = calcula_dolar(real, cotacao)
    print(dolar)

if __name__ == "__main__":
    main()