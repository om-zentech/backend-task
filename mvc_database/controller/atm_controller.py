from models.user import User
from models.atm import ATM

class ATMController:

    def create_user(self, name: str, bank: str, balance: float):

        user = User(name, bank, balance)
        card, pin = user.save()

        return {
            "success": True,
            "card": card,
            "pin": pin
        }

    def create_atm(self, atm_id: str, bank: str, balance: float):

        atm = ATM(atm_id, bank, balance)
        atm.save()

        return {
            "success": True,
            "message": "ATM created successfully"
        }

    def login(self, card: str, pin: str):

        user = User.authenticate(card, pin)

        if not user:
            return {
                "success": False,
                "message": "Invalid card or PIN"
            }

        return {
            "success": True,
            "data": user
        }
    

    def deposit(self, user_id: int, amount: float):

        if amount <= 0:
            return {
                "success": False,
                "message": "Invalid Deposit Amount!"
            }

        User.update_balance(user_id, amount)

        return {
            "success": True,
            "message": "Deposit Successful"
        }

    def withdraw(self, user_data, amount: float, atm_id: str):

        user_id, balance, bank_id, txn_count, total_withdrawal = user_data

        atm = ATM.get_atm(atm_id)

        if not atm:
            return {
                "success": False,
                "message": "Invalid ATM!"
            }

        atm_bank_id, atm_balance, per_limit, daily_limit, txn_limit = atm

        if txn_count >= txn_limit:
            return {
                "success": False,
                "message": "Transaction Limit Reached!"
            }

        if amount > per_limit:
            return {
                "success": False,
                "message": f"Per Transaction Limit Exceeded (Max: {per_limit})"
            }

        if total_withdrawal + amount > daily_limit:
            return {
                "success": False,
                "message": f"Daily Limit Exceeded (Max per day: {daily_limit})"
            }

        fee = 0
        if bank_id != atm_bank_id:
            fee = amount * 0.05

        total_deduction = amount + fee

        if balance < total_deduction:
            return {
                "success": False,
                "message": "Insufficient Balance!"
            }

        if atm_balance < amount:
            return {
                "success": False,
                "message": "ATM Out of Cash!"
            }

        User.update_balance(user_id, total_deduction, withdraw=True)
        ATM.update_balance(atm_id, amount)

        msg = f"Withdrawal Successful\nWithdrawn: {amount}"

        if fee:
            msg += f"\n5% Fee Applied: {fee}"

        return {
            "success": True,
            "message": msg
        }

    def show_balance(self, user_id: int):

        result = User.show_balance(user_id)

        if result:
            return {
                "success": True,
                "balance": result[0]
            }

        return {
            "success": False,
            "message": "User not found"
        }

    def show_account_details(self, user_id: int):

        data = User.show_account_details(user_id)

        if not data:
            return {
                "success": False,
                "message": "User not found"
            }

        return {
            "success": True,
            "data": data
        }