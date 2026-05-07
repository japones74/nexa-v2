from app.domain.game.engine import gerar_numero, resolver_jogo
from app.infrastructure.repositories.user_repository import UserRepository

repo = UserRepository()


def executar_aposta(user_id, escolha, valor, multiplicador):
    user = repo.buscar_usuario(user_id)
    if not user:
        return {"erro": "user_not_found"}

    numero = gerar_numero()
    result = resolver_jogo(escolha, numero, multiplicador)

    return {
        "numero": result.numero,
        "venceu": result.venceu,
        "janela": result.janela
    }
