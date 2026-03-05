from models.user import User
from models.atm import ATM

class TransactionController:

    PER_TRANSACTION_LIMIT = 10000
    DAILY_TRANSACTION_LIMIT = 25000
    MAX_TRANSACTIONS_PER_DAY = 3

    def deposit(self, user: User, atm: ATM, amount: float):

        if user.bank != atm.bank:
            return {"success": False, "message": "\nCan't Deposite with another Bank's ATM!"}

        if amount <= 0:
            return {"success": False, "message": "\nInvalid amount!"}

        user.deposit(amount)
        atm.deposit(amount)

        return {"success": True}

    def withdrawal(self, user: User, atm: ATM, amount: float):

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