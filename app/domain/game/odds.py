LIMITE_MAXIMO = 6999
HOUSE_EDGE = 0.13

MULTIPLICADORES = [
    2.0,
    3.0,
    5.0,
    9.0,
    13.0,
    47.0
]


def calcular_janela(multiplicador: float) -> int:
    if multiplicador not in MULTIPLICADORES:
        raise ValueError("invalid_multiplier")

    chance = (1 / multiplicador) * (1 - HOUSE_EDGE)

    return int((LIMITE_MAXIMO + 1) * chance)
