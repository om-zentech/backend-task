from controller.atm_controller import ATMContoller
from controller.user_contoller import UserController
from controller.transaction_controller import TransactionController
from models.user import User
from models.atm import ATM

class ATMView:

    def __init__(self):
        self.atm_controller = ATMContoller()
        self.user_controller = UserController()
        self.transaction_controller = TransactionController()

    def display_account_info(self, user):
        info = User.get_info(user)

        print('\n-----Account Details-----')
        for key, value in info.items():
            print(f'{key.capitalize().replace("_", " ")}: {value}')
        print()

    def setup_atms(self):

        atm_results = [
            self.atm_controller.create_atm("A01", "BOB", 200000),
            self.atm_controller.create_atm("A02", "HDFC", 300000)
        ]

        for result in atm_results:
            atm = result["atm"]
            print(f'\n-----ATM Created-----\n'
                  f'ID: {atm.id}\n'
                  f'Bank: {atm.bank.bank_name}\n'
                  f'ATM Balance: {atm.initial_balance}')
    
    def setup_banks(self):
        bank_names = ["BOB", "HDFC", "SBI"]

        for bank_name in bank_names:
            bank = self.atm_controller.create_bank(bank_name)
            print(f'\n-----Bank Created-----\n'
                  f'Name: {bank.bank_name}')

    def user_flow(self):

        while True:
            try:
                name = input('\nEnter User Name: ')
                bank_name = input('Enter Bank Name: ')
                balance = float(input('Enter Balance: '))

                result = self.user_controller.create_user(name, bank_name, balance)

                if not result["success"]:
                    print(result["message"])
                    continue

                user = result["user"]

                print(f'\n----- User Created -----\n'
                      f'Name: {user.name}\n'
                      f'Bank: {user.bank.bank_name}\n'
                      f'Card Number: {user.card_number}\n'
                      f'Pin: {result["pin"]}\n'
                      f'Balance: {user.balance}\n')

                return user

            except ValueError:
                print('\nInvalid Input, try again!\n')

    def select_atm(self):

        while True:
            print("\nAvailable ATMs:")
            for atm_id, atm in ATM.atms.items():
                print(f"{atm_id} - {atm.bank.bank_name}")

            atm_id = input('\nSelect ATM ID for transaction: ')
            atm = ATM.get_atm(atm_id)

            if not atm:
                print('\nATM not exist, try again!\n')
            else:
                return atm

    def login_flow(self):

        while True:
            card_number = input('Enter Card Number: ')
            pin_number = input('Enter Pin: ')

            user = User.get_user(card_number)

            if not user:
                print('\nUser not exist, try again!\n')
                continue

            if user.pin_number != pin_number:
                print('\nIncorrect pin, try again!\n')
                continue

            return user

    def operation_menu(self, user, atm):

        while True:
            print('\n-----Select Operation-----\n'
                  '1.Deposite\n'
                  '2.Withdraw\n'
                  '3.Check bank balance\n'
                  '4.Get account details\n'
                  '5.Update your details\n'
                  '6.Delete Account\n'
                  '7.Exit')

            choice = input('\nEnter Choice: ')

            if choice == '1':
                try:
                    amount = float(input('\nEnter amount to be deposit: '))
                    result = self.transaction_controller.deposit(user, atm, amount)

                    if result["success"]:
                        print('\n----- Money Successfully Deposited to your account -----\n')
                        self.display_account_info(user)
                    else:
                        print(result["message"])

                except ValueError:
                    print('Invalid Input!')

            elif choice == '2':
                try:
                    amount = float(input('\nEnter amount to be withdrawal: '))
                    result = self.transaction_controller.withdrawal(user, atm, amount)

                    if result["success"]:
                        print('\n----- Money Successfully Withdraw from your Account -----\n')
                        self.display_account_info(user)

                        if result.get("fee", 0) > 0:
                            print('\n5% transaction fee applied.')
                    else:
                        print(result["message"])

                except ValueError:
                    print('Invalid Input!')

            elif choice == '3':
                print(f'\nAvailable Balance: {user.balance}\n')

            elif choice == '4':
                self.display_account_info(user)

            elif choice == '5':
                while True:
                    print('\n-----Select Detail to Update-----\n'
                        '1.Name\n'
                        '2.Pin\n'
                        '3.Exit')

                    update_choice = input('Enter Choice: ')

                    if update_choice == '1':
                        new_name = input('Enter new name: ')
                        result = self.user_controller.update_user(user, "name", new_name)
                        print(result["message"])

                    elif update_choice == '2':
                        result = self.user_controller.update_user(user, "pin")
                        print(result["message"])

                    elif update_choice == '3':
                        break

                    else:
                        print('Invalid Input, try again!')

            elif choice == '6':
                result = self.user_controller.delete_user(user.card_number)
                print(result["message"])
                if result["success"]:
                    break

            elif choice == '7':
                break

            else:
                print('Invalid Input, try again!')

    def menu(self):

        self.setup_atms()
        self.setup_banks()
        self.user_flow()
        
        logged_user = self.login_flow()
        atm = self.select_atm()

        self.operation_menu(logged_user, atm)