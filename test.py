from app.domain.game.engine import gerar_numero, calcular_resultado
from app.domain.game.odds import MULTIPLICADORES

APOSTA = 0.10
SIMULACOES = 1_000_000


def testar(mult):
    saldo = 0.0
    wins = 0

    for _ in range(SIMULACOES):
        saldo -= APOSTA

        numero = gerar_numero()
        resultado = calcular_resultado("LO", numero, mult)

        if resultado.venceu:
            saldo += APOSTA * mult
            wins += 1

    edge = (-saldo / (SIMULACOES * APOSTA)) * 100

    print(f"{mult}x")
    print(f"wins: {wins}")
    print(f"house edge real: {edge:.4f}%")
    print("-" * 30)


for mult in MULTIPLICADORES:
    testar(mult)
