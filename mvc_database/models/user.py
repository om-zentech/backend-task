import random
from models.database import Database
from models.bank import Bank

class User:

    def __init__(self, name: str, bank_name: str, balance: float):
        self.name = name
        self.bank_name = bank_name
        self.balance = balance
        self.card_number = self.generate_card()
        self.pin = self.generate_pin()

    @staticmethod
    def generate_pin():
        return str(random.randint(1000, 9999))

    @staticmethod
    def generate_card():
        return str(random.randint(10**15, (10**16) - 1))

    def save(self):

        bank = Bank(self.bank_name)
        bank.save()
        bank_id = Bank.get_bank_id(self.bank_name)

        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO users(name,card_number,pin,balance,bank_id) VALUES(%s,%s,%s,%s,%s);
        """, (self.name, self.card_number, self.pin, self.balance, bank_id))

        conn.commit()
        cur.close()
        conn.close()

        return self.card_number, self.pin

    @staticmethod
    def authenticate(card: str, pin: str):

        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("""
        SELECT id,balance,bank_id,count_of_transaction,total_withdrawal
        FROM users
        WHERE card_number=%s AND pin=%s;
        """, (card, pin))

        user = cur.fetchone()

        cur.close()
        conn.close()

        return user

    @staticmethod
    def show_balance(user_id: int):

        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("SELECT balance FROM users WHERE id=%s;", (user_id,))
        result = cur.fetchone()

        cur.close()
        conn.close()

        return result

    @staticmethod
    def show_account_details(user_id: int):

        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("""
        SELECT u.name,u.card_number,u.balance,
        u.count_of_transaction,u.total_withdrawal,b.bank_name
        FROM users u
        JOIN banks b ON u.bank_id=b.id
        WHERE u.id=%s;
        """, (user_id,))

        user = cur.fetchone()

        cur.close()
        conn.close()

        return user

    @staticmethod
    def update_balance(user_id: int, amount: float, withdraw: bool = False):

        db = Database()
        conn = db.connect()
        cur = conn.cursor()

        if withdraw:
            cur.execute("""
            UPDATE users
            SET balance = balance - %s,
            count_of_transaction = count_of_transaction + 1,
            total_withdrawal = total_withdrawal + %s
            WHERE id=%s;
            """, (amount, amount, user_id))

        else:
            cur.execute("""
            UPDATE users
            SET balance = balance + %s
            WHERE id=%s;
            """, (amount, user_id))

        conn.commit()
        cur.close()
        conn.close()