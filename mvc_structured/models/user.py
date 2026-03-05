import random

class User:
    users = {}

    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance
        self.card_number = self.generate_card_number()
        self.pin_number = self.generate_pin()
        self.count_of_transaction = 0
        self.total_withdrawal = 0

        User.users[self.card_number] = self

    @staticmethod
    def generate_pin():
        return str(random.randint(1000, 9999))

    @staticmethod
    def generate_card_number():
        return str(random.randint(10**15, (10**16) - 1))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        self.count_of_transaction += 1
        self.total_withdrawal += amount

    def get_info(self):
        return {
            "name": self.name,
            "bank": self.bank.bank_name,
            "card_number": self.card_number,
            "balance": self.balance
        }

    @classmethod
    def get(cls, card_number):
        return cls.users.get(card_number)