from models.user import User
from models.bank import Bank
from models.atm import ATM

class Management:

    PER_TRANSACTION_LIMIT = 10000
    DAILY_TRANSACTION_LIMIT = 25000
    MAX_TRANSACTIONS_PER_DAY = 3

    def create_bank(self, bank_name):
        bank = Bank.get(bank_name)
        if not bank:
            bank = Bank(bank_name)
        return bank

    def create_user(self, name, bank_name, balance):
        if balance < 0:
            return {"success": False, "message": "Balance cannot be negative, try again!"}

        bank = self.create_bank(bank_name)
        user = User(name, bank, balance)

        return {
            "success": True,
            "user": user,
            "pin": user.pin_number
        }
        
    def delete_user(self, card_number):

        user = User.users.get(card_number)

        if not user:
            return {
                "success": False,
                "message": "User not found!"
            }

        del User.users[card_number]

        return {
            "success": True,
            "message": "\nAccount deleted successfully!"
        }

    def update_user(self, user, field, new_value=None):

        if field == "name":
            user.name = new_value
            return {"success": True, "message": "\nName updated successfully!"}

        elif field == "pin":
            user.pin_number = user.generate_pin()
            return {"success": True, "message": f"\nNew PIN: {user.pin_number}"}
        else:
            return {"success": False, "message": "\nInvalid field!"}
    
    def create_atm(self, atm_id, bank_name, balance):
        bank = self.create_bank(bank_name)
        atm = ATM(atm_id, bank, balance)
        return {"success": True, "atm": atm}

    def deposit(self, user, atm, amount):

        if user.bank != atm.bank:
            return {"success": False, "message": "\nCan't Deposite with another Bank's ATM!"}

        if amount <= 0:
            return {"success": False, "message": "\nInvalid amount!"}

        user.deposit(amount)
        atm.deposit(amount)

        return {"success": True}

    def withdrawal(self, user, atm, amount):

        if amount <= 0:
            return {"success": False, "message": "\nInvalid amount!"}

        if user.count_of_transaction >= self.MAX_TRANSACTIONS_PER_DAY:
            return {"success": False, "message": "\nTransaction count limit reached for today!"}

        if amount > self.PER_TRANSACTION_LIMIT:
            return {"success": False, "message": "\nPer transaction limit reached!"}

        if (user.total_withdrawal + amount) > self.DAILY_TRANSACTION_LIMIT:
            return {"success": False, "message": "\nWithdrawal limit reached for today!"}

        fee = 0

        if user.bank != atm.bank:
            fee = amount * 0.05

        total_deduction = amount + fee

        if user.balance < total_deduction:
            return {"success": False, "message": "\nInsufficient balance!"}

        if atm.initial_balance < amount:
            return {"success": False, "message": "\nInsufficient ATM balance!"}

        user.withdraw(total_deduction)
        atm.withdraw(amount)

        return {"success": True, "fee": fee}