import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class Database:

    def __init__(self):
        self.host_name = os.getenv("DB_HOST")
        self.database_name = os.getenv("DB_NAME")
        self.user_name = os.getenv("DB_USER")
        self.user_pass = os.getenv("DB_PASS")

    def connect(self):

        return psycopg2.connect(
            host=self.host_name,
            database=self.database_name,
            user=self.user_name,
            password=self.user_pass
        )

    def setup_database(self):

        conn = self.connect()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS banks(
            id SERIAL PRIMARY KEY,
            bank_name VARCHAR(150) UNIQUE NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(150),
            card_number VARCHAR(16) UNIQUE,
            pin VARCHAR(4),
            balance FLOAT,
            bank_id INTEGER REFERENCES banks(id),
            count_of_transaction INTEGER DEFAULT 0,
            total_withdrawal FLOAT DEFAULT 0
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS atms(
            id VARCHAR(10) PRIMARY KEY,
            bank_id INTEGER REFERENCES banks(id),
            balance FLOAT,
            per_transaction_limit FLOAT DEFAULT 10000,
            daily_transaction_limit FLOAT DEFAULT 25000,
            no_of_transaction_per_day INTEGER DEFAULT 3
        );
        """)

        conn.commit()
        cur.close()
        conn.close()