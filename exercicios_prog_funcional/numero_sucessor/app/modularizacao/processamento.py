def processamento(operacao: str, numero:int) -> float:
    if operacao == "a":
        antecessor = numero -1
        return antecessor
    elif operacao == "s":
        sucessor = numero + 1
        return sucessor
    else:
        print("Você não digitou 'a' nem 'b'.")