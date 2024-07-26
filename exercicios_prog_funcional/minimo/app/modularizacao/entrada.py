def entrada() -> tuple[str, float, float]:
    operacao = input("'m' para mínimo e 'M' para máximo: ")
    a = float(input("Digite o primeiro número real: "))
    b = float(input("Digite o segundo número real: "))
    return operacao, a, b
