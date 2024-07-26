from entrada import entrada
from calcula_exponencial import calcula_exponencial
from saida import saida

def main() -> None:
    expoente, x, y = entrada()
    resultado = calcula_exponencial(expoente, x, y)
    saida(resultado)

if __name__ == "__main__":
    main()