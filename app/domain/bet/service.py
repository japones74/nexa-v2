from dataclasses import dataclass
from app.domain.game.engine import gerar_numero, calcular_resultado
from app.domain.wallet.wallet import Wallet, Balance


@dataclass
class BetRequest:
    user_id: int
    escolha: str
    valor: int
    multiplicador: float


@dataclass
class BetResult:
    numero: int
    venceu: bool
    lucro: int
    saldo: dict
    usados: dict


class BetService:
    def __init__(self):
        self.wallet = Wallet()

    def executar(self, request: BetRequest, balance: Balance) -> BetResult:
        balance, usados = self.wallet.debitar(balance, request.valor)

        resultado = gerar_numero()
        game = calcular_resultado(
            request.escolha,
            resultado,
            request.multiplicador
        )

        lucro = 0

        if game.venceu:
            lucro = int(request.valor * request.multiplicador)
            balance = self.wallet.creditar(balance, lucro)

        return BetResult(
            numero=game.numero,
            venceu=game.venceu,
            lucro=lucro,
            saldo=self.wallet.snapshot(balance),
            usados=usados
        )
