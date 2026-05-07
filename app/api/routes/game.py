from flask import Blueprint, request, jsonify
from app.domain.game.service import executar_aposta

game = Blueprint("game", __name__)


@game.route("/api/game/apostar", methods=["POST"])
def apostar():
    data = request.get_json()

    return jsonify(
        executar_aposta(
            data["user_id"],
            data["escolha"],
            data["valor"],
            data["multiplicador"]
        )
    )
