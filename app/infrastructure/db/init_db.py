from app.infrastructure.db.connection import get_connection


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            saldo_real INTEGER DEFAULT 10000,
            saldo_bonus INTEGER DEFAULT 0,
            saldo_locked INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()
