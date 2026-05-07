from app.infrastructure.db.connection import get_connection


class Wallet:
    def get_user(self, user_id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cur.fetchone()

        conn.close()
        return user

    def get_balance(self, user_id):
        user = self.get_user(user_id)

        if not user:
            return 0

        return (
            (user["saldo_real"] or 0)
            + (user["saldo_bonus"] or 0)
            + (user["saldo_locked"] or 0)
        )
