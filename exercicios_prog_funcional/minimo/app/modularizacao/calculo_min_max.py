def calculo_min_max(operacao: str, a: float, b: float) -> float:
    if operacao == "m" and a < b:
        return a
    elif operacao == "m" and a > b:
        return b
    elif operacao == "M" and a < b:
        return b
    elif operacao == "M" and a > b:
        return a
    elif a == b:
        raise ValueError(f"{a}={b}.")
    else:
        raise ValueError(f"'{operacao}' não válida.")