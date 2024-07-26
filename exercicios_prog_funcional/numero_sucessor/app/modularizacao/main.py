from entrada import entrada
from processamento import processamento
from saida import saida

def main() -> None:
    operacao, numero = entrada()
    resultado = processamento(operacao, numero)
    saida(resultado)

if __name__ == "__main__":
    main()