from models.database import Database
from models.bank import Bank

class ATM:

    def __init__(self, atm_id: str, bank_name: str, balance: float):
        self.atm_id = atm_id
        self.bank_name = bank_name
        self.balance = balance

    def save(self):

        bank = Bank(self.bank_name)
        bank.save()
        bank_id = Bank.get_bank_id(self.bank_name)

        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO atms(id,bank_id,balance)
        VALUES(%s,%s,%s) ON CONFLICT(id) DO NOTHING;
        """, (self.atm_id, bank_id, self.balance))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_atm(atm_id: str):
        
        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("""
        SELECT bank_id,balance,per_transaction_limit,
        daily_transaction_limit,no_of_transaction_per_day
        FROM atms WHERE id=%s;
        """, (atm_id,))

        atm = cur.fetchone()

        cur.close()
        conn.close()

        return atm
    

    @staticmethod
    def update_balance(atm_id: str, amount: float):

        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("""
        UPDATE atms
        SET balance = balance - %s WHERE id=%s;
        """, (amount, atm_id))

        conn.commit()
        cur.close()
        conn.close()