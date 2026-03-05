from models.bank import Bank
from models.atm import ATM

class ATMContoller:
    def create_bank(self, bank_name):
        bank = Bank.get_bank(bank_name)
        if not bank:
            bank = Bank(bank_name)
        return bank
    
    def create_atm(self, atm_id, bank_name, balance):
        bank = self.create_bank(bank_name)
        atm = ATM(atm_id, bank, balance)
        return {"success": True, "atm": atm}