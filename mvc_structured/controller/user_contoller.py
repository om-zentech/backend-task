from models.user import User
from models.bank import Bank

class UserController:

    def create_user(self, name: str, bank_name: str, balance: float):
        if balance < 0:
            return {"success": False, "message": "\nCannot create user with negative balance, try again!"}        
        bank = Bank.get_bank(bank_name)
        if not bank:
            return {"success": False, "message": "\nBank not found, try again!"}
        user = User(name, bank, balance)

        return {
            "success": True,
            "user": user,
            "pin": user.pin_number
        }
        
    def delete_user(self, card_number):
        user = User.get_user(card_number)

        if not user:
            return {
                "success": False,
                "message": "User not found!"
            }

        user.del_user()

        return {
            "success": True,
            "message": "\nAccount deleted successfully!"
        }

    def update_user(self, user:User, field, new_value=None):

        if field == "name":
            if not new_value:
                return {"success": False, "message": "\nName cannot be empty!"}
            else:
                user.name = new_value
                return {"success": True, "message": "\nName updated successfully!"}

        elif field == "pin":
            user.pin_number = user.generate_pin()
            return {"success": True, "message": f"\nNew PIN: {user.pin_number}"}
        else:
            return {"success": False, "message": "\nInvalid field!"}