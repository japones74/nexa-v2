from app.infrastructure.db.connection import get_connection, transactional
from app.domain.wallet.wallet import Balance


class UserRepository:
    def __init__(self):
        self.db_path = "nexa.db"

    def get_balance(self, user_id: int) -> Balance:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT saldo_real, saldo_bonus, saldo_locked FROM users WHERE id = ?",
            (user_id,)
        )

        row = cur.fetchone()
        conn.close()

        if not row:
            return Balance()

        return Balance(
            real=int(row["saldo_real"] or 0),
            bonus=int(row["saldo_bonus"] or 0),
            locked=int(row["saldo_locked"] or 0),
        )

    @transactional
    def save_balance(self, conn, user_id: int, balance: Balance):
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE users
            SET saldo_real = ?,
                saldo_bonus = ?,
                saldo_locked = ?
            WHERE id = ?
            """,
            (balance.real, balance.bonus, balance.locked, user_id)
        )
