def entrada() -> tuple[str, float]:
    operacao = input("Digite 'a' para antecessor e 's' para sucessor: ")
    numero = int(input("Digite um número inteiro: "))
    return operacao, numero