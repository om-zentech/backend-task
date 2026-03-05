from models.database import Database

class Bank:

    def __init__(self, bank_name: str):
        self.bank_name = bank_name

    def save(self):
        
        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO banks(bank_name) VALUES(%s) ON CONFLICT(bank_name) DO NOTHING;
        """, (self.bank_name,))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_bank_id(bank_name: str):

        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute(
            "SELECT id FROM banks WHERE bank_name=%s;",
            (bank_name,)
        )

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0] if result else None