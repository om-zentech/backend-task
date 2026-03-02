import psycopg2
import random

class Database:
    host_name = "localhost"
    database_name = "atm_task"
    user_name = "postgres"
    user_pass = "om22"

    @classmethod
    def connect(cls):
        return psycopg2.connect(
            host=cls.host_name,
            database=cls.database_name,
            user=cls.user_name,
            password=cls.user_pass)

    @classmethod
    def setup_connection(cls):
        conn = cls.connect()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS banks(
            id SERIAL PRIMARY KEY,
            bank_name VARCHAR(150) UNIQUE NOT NULL);""")

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(150),
            card_number VARCHAR(16) UNIQUE,
            pin VARCHAR(4),
            balance FLOAT,
            bank_id INTEGER REFERENCES banks(id),
            count_of_transaction INTEGER DEFAULT 0,
            total_withdrawal FLOAT DEFAULT 0);""")

        cur.execute("""
        CREATE TABLE IF NOT EXISTS atms(
            id VARCHAR(10) PRIMARY KEY,
            bank_id INTEGER REFERENCES banks(id),
            balance FLOAT,
            per_transaction_limit FLOAT DEFAULT 10000,
            daily_transaction_limit FLOAT DEFAULT 25000,
            no_of_transaction_per_day INTEGER DEFAULT 3);""")

        conn.commit()
        cur.close()
        conn.close()

class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name

    def save(self):
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO banks(bank_name)
        VALUES(%s)  ON CONFLICT(bank_name) DO NOTHING;
        """, (self.bank_name,))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_bank_id(bank_name):
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("SELECT id FROM banks WHERE bank_name=%s;",(bank_name,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        return result[0] if result else None

class User:

    def __init__(self, name, bank_name, balance):
        self.name = name
        self.bank_name = bank_name
        self.balance = balance
        self.card_number = self.generate_card()
        self.pin = self.generate_pin()

    @staticmethod
    def generate_pin():
        return str(random.randint(1000, 9999))

    @classmethod
    def generate_card(cls):
        return str(random.randint(10**15, (10**16) - 1))

    def save(self):
        bank = Bank(self.bank_name)
        bank.save()
        bank_id = Bank.get_bank_id(self.bank_name)
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO users(name, card_number, pin, balance, bank_id)
        VALUES(%s,%s,%s,%s,%s);""", (self.name, self.card_number, self.pin, self.balance, bank_id))
        conn.commit()
        cur.close()
        conn.close()
        print("\nUser Created Successfully")
        print("Card:", self.card_number)
        print("PIN:", self.pin)
        
    @staticmethod
    def show_balance(user_id):
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT balance
            FROM users
            WHERE id = %s;
        """, (user_id,))

        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            print("\n----- Current Balance -----")
            print("Available Balance:", result[0])
        else:
            print("User not found.")

    @staticmethod
    def show_account_details(user_id):
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT u.name,
                u.card_number,
                u.balance,
                u.count_of_transaction,
                u.total_withdrawal,
                b.bank_name
            FROM users u JOIN banks b ON u.bank_id = b.id WHERE u.id = %s; """, (user_id,))
        user = cur.fetchone()

        cur.close()
        conn.close()
        if user:
            print("\n----- Account Details -----")
            print("Name:", user[0])
            print("Card Number:", user[1])
            print("Bank:", user[5])
            print("Balance:", user[2])
            print("Transaction Count:", user[3])
            print("Total Withdrawal Today:", user[4])
        else:
            print("User not found.")

    @staticmethod
    def authenticate(card, pin):
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("""
        SELECT id, balance, bank_id, count_of_transaction, total_withdrawal FROM users
        WHERE card_number=%s AND pin=%s;""", (card, pin))
        user = cur.fetchone()

        cur.close()
        conn.close()
        return user

    @staticmethod
    def update_balance(user_id, amount, withdraw=False):
        conn = Database.connect()
        cur = conn.cursor()
        if withdraw:
            cur.execute("""
            UPDATE users SET balance = balance - %s,
                count_of_transaction = count_of_transaction + 1,
                total_withdrawal = total_withdrawal + %s
            WHERE id = %s;
            """, (amount, amount, user_id))
        else:
            cur.execute("""
            UPDATE users
            SET balance = balance + %s
            WHERE id = %s;
            """, (amount, user_id))

        conn.commit()
        cur.close()
        conn.close()

class ATM:

    def __init__(self, atm_id, bank_name, balance):
        self.atm_id = atm_id
        self.bank_name = bank_name
        self.balance = balance

    def save(self):
        bank = Bank(self.bank_name)
        bank.save()
        bank_id = Bank.get_bank_id(self.bank_name)
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO atms(id, bank_id, balance)
        VALUES(%s,%s,%s)
        ON CONFLICT(id) DO NOTHING;
        """, (self.atm_id, bank_id, self.balance))

        conn.commit()
        cur.close()
        conn.close()
        print("ATM Created Successfully")

    @staticmethod
    def get_atm(atm_id):
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("""
        SELECT bank_id, balance, per_transaction_limit,
               daily_transaction_limit, no_of_transaction_per_day
        FROM atms WHERE id=%s;
        """, (atm_id,))
        atm = cur.fetchone()
        cur.close()
        conn.close()
        return atm

    @staticmethod
    def update_balance(atm_id, amount):
        conn = Database.connect()
        cur = conn.cursor()
        cur.execute("""
        UPDATE atms
        SET balance = balance - %s
        WHERE id=%s;
        """, (amount, atm_id))
        conn.commit()
        cur.close()
        conn.close()

class ATMSystem:

    @staticmethod
    def deposit(user_id):
        amount = float(input("\nEnter Deposit Amount: "))
        User.update_balance(user_id, amount)
        print("\nDeposit Successful")

    @staticmethod
    def withdraw(user_data):
        user_id, balance, bank_id, txn_count, total_withdrawal = user_data
        try:
            amount = float(input("Enter Withdraw Amount: "))
        except ValueError:
            print("\nInvalid amount!\n")
            return
        if amount <= 0:
            print("\nWithdrawal amount must be greater than 0!\n")
            return
        if amount != round(amount, 2):
            print("\nOnly 2 decimal places allowed!\n")
            return
        if amount > 1_000_000:
            print("\nAmount too large!\n")
            return
        atm_id = input("Enter ATM ID: ").strip()
        if not atm_id:
            print("\nATM ID cannot be empty!\n")
            return
        atm = ATM.get_atm(atm_id)
        if not atm:
            print("\nInvalid ATM!\n")
            return
        atm_bank_id, atm_balance, per_limit, daily_limit, txn_limit = atm
        if txn_count >= txn_limit:
            print("\nTransaction Limit Reached!\n")
            return
        if amount > per_limit:
            print(f"\nPer Transaction Limit Exceeded (Max: {per_limit})\n")
            return
        if total_withdrawal + amount > daily_limit:
            print(f"\nDaily Limit Exceeded (Max per day: {daily_limit})\n")
            return
        fee = 0
        if bank_id != atm_bank_id:
            fee = amount * 0.05
        total_deduction = amount + fee
        if balance < total_deduction:
            print("\nInsufficient Balance!\n")
            return
        if atm_balance < amount:
            print("\nATM Out of Cash!\n")
            return
        User.update_balance(user_id, total_deduction, withdraw=True)        
        ATM.update_balance(atm_id, amount)
        print("\nWithdrawal Successful")
        print("Withdrawn:", amount)
        if fee:
            print(f"\n5% Fee Applied: {fee}\n")

class MainRun:
    
    @staticmethod
    def main():
        Database.setup_connection()
        while True:
            print("\n==== ATM SYSTEM ====")
            print("1. Create User")
            print("2. Create ATM")
            print("3. Login")
            print("4. Exit")
            choice = input("\nEnter Choice: ")
            if choice == "1":
                name = input("Name: ")
                bank = input("Bank: ")
                balance = float(input("Balance: "))
                user = User(name, bank, balance)
                user.save()
            elif choice == "2":
                atm_id = input("ATM ID: ")
                bank = input("Bank: ")
                balance = float(input("ATM Balance: "))
                atm = ATM(atm_id, bank, balance)
                atm.save()
            elif choice == "3":
                card = input("Card Number: ")
                pin = input("PIN: ")
                user = User.authenticate(card, pin)
                if not user:
                    print("\nInvalid Credentials!")
                    continue
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Show Balance")
                    print("4. Show Account Details")
                    print("5. Logout")
                    op = input("Enter Choice: ")
                    if op == "1":
                        ATMSystem.deposit(user[0])
                    elif op == "2":
                        ATMSystem.withdraw(user)
                    elif op == "3":
                        User.show_balance(user[0])
                    elif op == "4":
                        User.show_account_details(user[0])
                    elif op == "5":
                        break
                    else:
                        print("\nInvalid Option!")
            elif choice == "4":
                print("\nExiting...")
                break
            else:
                print("\nInvalid Choice!")
run_main = MainRun()
run_main.main()