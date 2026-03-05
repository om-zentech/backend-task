class ATM:
    atms = {}

    def __init__(self, id, bank, initial_balance):
        self.id = id
        self.bank = bank
        self.initial_balance = initial_balance

        ATM.atms[id] = self

    def deposit(self, amount):
        self.initial_balance += amount

    def withdraw(self, amount):
        self.initial_balance -= amount

    @classmethod
    def get_atm(cls, atm_id):
        return cls.atms.get(atm_id)