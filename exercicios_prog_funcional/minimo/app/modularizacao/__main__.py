from entrada import entrada
from calculo_min_max import calculo_min_max

def main() -> None:
    try:
        operacao, a, b = entrada()
        min_max = calculo_min_max(operacao, a, b)
        print(min_max)
    except ValueError as e:
        print(f"{e}")

if __name__ == "__main__":
    main()