from entrada import entrada
from calcula_produto import calcula_produto
from saida import saida

def main():
    x, y = entrada()
    produto = calcula_produto(x, y)
    print(produto)

if __name__ == "__main__":
    main()