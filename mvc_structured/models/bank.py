class Bank:
    banks = {}

    def __init__(self, bank_name):
        self.bank_name = bank_name
        Bank.banks[bank_name] = self
    
    @classmethod
    def get_bank(cls, bank_name):
        return cls.banks.get(bank_name)