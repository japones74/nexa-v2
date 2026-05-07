from dataclasses import dataclass
import random

from app.domain.game.odds import LIMITE_MAXIMO, calcular_janela


@dataclass(frozen=True)
class GameResult:
    numero: int
    venceu: bool
    janela: int
    escolha: str


def gerar_numero() -> int:
    return random.randint(0, LIMITE_MAXIMO)


def calcular_resultado(
    escolha: str,
    numero: int,
    multiplicador: float
) -> GameResult:
    janela = calcular_janela(multiplicador)

    if escolha == "LO":
        venceu = numero <= janela
    elif escolha == "HI":
        venceu = numero >= (LIMITE_MAXIMO - janela)
    else:
        raise ValueError("invalid_choice")

    return GameResult(
        numero=numero,
        venceu=venceu,
        janela=janela,
        escolha=escolha
    )
