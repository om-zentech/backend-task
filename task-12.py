'''
Create an ATM machine
- User should be able get money out of it
- User should be able to deposite money into it
- You must ask card number and pin before any transaction
- User can get overall information about his bank account
- There should be a limit in one time transaction and total transaction in a day (Consider day as from starting of script to exit)
- Limit on number of transaction
- Let user choose the bank of ATM
- Every ATM will have some initial balance
- Every user has it's own bank
- If user takes money from an ATM other than his bank take 5% cut in withdrawl amount
Nice to have features:
- Insert, update and delete users (Generate card number and PIN randomly)
- Insert, update and delete ATMs
- Insert, update and delete banks
- Insert money into ATM (No database is needed for this it can be managed using dicts)
Hint: You can manage all this with data dictionary data type.
'''
import random

class User:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance
        self.card_number = self.generate_card_number()
        self.pin_number = self.generate_pin()
        self.count_of_transaction = 0
        self.total_withdrawal = 0

    @staticmethod
    def generate_pin():
        return str(random.randint(1000, 9999))

    @classmethod
    def generate_card_number(cls):
        return str(random.randint(10**15, (10**16) - 1))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        self.count_of_transaction += 1
        self.total_withdrawal += amount

    def display_info(self):
        print(f'\n-----Account Details-----\n'
              f'Name: {self.name}\n'
              f'Bank: {self.bank.bank_name}\n'
              f'Card Number: {self.card_number}\n'
              f'Balance: {self.balance}\n')

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.users = {}
        self.atms = {}

    def add_user(self, user):
        self.users[user.card_number] = user

    def add_atm(self, atm):
        self.atms[atm.id] = atm


class ATM:
    def __init__(self, id, bank, initial_balance):
        self.id = id
        self.bank = bank
        self.initial_balance = initial_balance
        self.per_transaction_limit = 10000
        self.daily_transaction_limit = 25000
        self.no_of_transaction_per_day = 3

    @classmethod
    def deposit(cls, atm_obj, amount):
        atm_obj.initial_balance += amount

    @classmethod
    def withdraw(cls, atm_obj, amount):
        atm_obj.initial_balance -= amount

class Management:
    def __init__(self):
        self.atms = {}
        self.banks = {}
        self.users = {}

    def create_bank(self, bank_name):
        if bank_name not in self.banks:
            self.banks[bank_name] = Bank(bank_name)
        return self.banks[bank_name]

    def create_user(self, user_data):
        self.users[user_data.card_number] = user_data
        user_data.bank.add_user(user_data)

        print(f'\n----- User Created -----\n'
              f'Name: {user_data.name}\n'
              f'Bank: {user_data.bank.bank_name}\n'
              f'Card Number: {user_data.card_number}\n'
              f'Pin: {user_data.pin_number}\n'
              f'Balance: {user_data.balance}\n')

    def create_atm(self, atm_data):
        self.atms[atm_data.id] = atm_data
        atm_data.bank.add_atm(atm_data)

        print(f'\n-----ATM Created-----\n'
              f'ID: {atm_data.id}\n'
              f'Bank: {atm_data.bank.bank_name}\n'
              f'ATM Balance: {atm_data.initial_balance}\n')

    def create_user_input(self):
        while True:
            try:
                name = input('Enter User Name: ')
                bank_name = input('Enter Bank Name: ')
                balance = float(input('Enter Balance: '))

                if balance < 0:
                    print('Balance cannot be negative, try again!')
                    continue

                bank = self.create_bank(bank_name)
                user_data = User(name, bank, balance)
                self.create_user(user_data)
                break

            except ValueError:
                print('\nInvalid Input, try again!\n')

    def update_user(self, user_data):
        while True:
            print('\n-----Select Detail to Update-----\n1.Name\n2.Bank Name\n3.Pin\n4.Exit\n')
            input_choice = input('Enter Choice: ')

            if input_choice == '1':
                user_data.name = input('Enter new name: ')
                user_data.display_info()

            elif input_choice == '2':
                new_bank_name = input('Enter new bank name: ')
                bank = self.create_bank(new_bank_name)
                user_data.bank = bank
                user_data.display_info()

            elif input_choice == '3':
                user_data.pin_number = User.generate_pin()
                print(f'----- PIN Updated Successfully -----\n'
                      f'New PIN: {user_data.pin_number}\n')

            elif input_choice == '4':
                break
            else:
                print('Invalid Input, try again!')

    def main_menu(self):
        self.create_user_input()

        while True:
            input_atm_id = input('Select ATM ID for transaction: ')
            if input_atm_id not in self.atms:
                print('ATM not exist,try again!\n')
            else:
                break

        while True:
            input_card_number = input('Enter Card Number: ')
            input_pin_number = input('Enter Pin: ')

            if input_card_number not in self.users:
                print('\nUser not exist, try again!\n')
                continue
            elif self.users[input_card_number].pin_number != input_pin_number:
                print('\nIncorrect pin, try again!\n')
                continue
            else:
                break

        user_data = self.users[input_card_number]
        atm_data = self.atms[input_atm_id]

        while True:
            print('\n-----Select Operation-----\n1.Deposite\n2.Withdraw\n3.Check bank balance\n4.Get account details\n5.Update your details\n6.Exit')
            input_choice = input('\nEnter Choice: ')

            if input_choice == '1':
                self.deposit(user_data, atm_data)
            elif input_choice == '2':
                self.withdrawal(user_data, atm_data)
            elif input_choice == '3':
                print(f'\nAvailable Balance: {user_data.balance}\n')
            elif input_choice == '4':
                user_data.display_info()
            elif input_choice == '5':
                self.update_user(user_data)
            elif input_choice == '6':
                break
            else:
                print('Invalid Input, try again!')
    
    @staticmethod
    def deposit(user_data, atm_data):
        try:
          if user_data.bank == atm_data.bank:
            amount = float(input('\nEnter amount to be deposit: '))
            if amount <= 0:
                print('Invalid amount!')
                return

            user_data.deposit(amount)
            ATM.deposit(atm_data,amount)

            print('\n----- Money Successfully Deposited to your account -----\n')
            user_data.display_info()
          else:
            print('\nCan\'t Deposite with another Bank\'s ATM!')

        except ValueError:
            print('Invalid Input!')

    @staticmethod
    def withdrawal(user_data, atm_data):
        try:
            amount = float(input('\nEnter amount to be withdrawal: '))
            if amount <= 0:
                print('Invalid amount!')
                return

            if user_data.count_of_transaction >= atm_data.no_of_transaction_per_day:
                print('\nTransaction count limit reached for today!')
                return

            if amount > atm_data.per_transaction_limit:
                print('\nPer transaction limit reached for today!')
                return

            if (user_data.total_withdrawal + amount) > atm_data.daily_transaction_limit:
                print('\nWithdrawal limit reached for today!')
                return

            fee = 0
            if user_data.bank.bank_name != atm_data.bank.bank_name:
                fee = amount * 0.05

            total_deduction = amount + fee

            if user_data.balance < total_deduction:
                print('\nInsufficient balance!')
                return

            if atm_data.initial_balance < total_deduction:
                print('\nInsufficient ATM balance!')
                return

            user_data.withdraw(total_deduction)
            ATM.withdraw(atm_data, amount)

            print('\n----- Money Successfully Withdraw from your Account -----\n')
            user_data.display_info()

            if fee > 0:
                print('5% transaction fee applied.')

        except ValueError:
            print('Invalid Input!')

manage_task = Management()

bank1 = manage_task.create_bank('BOB')
bank2 = manage_task.create_bank('HDFC')

atm_1 = ATM('A01', bank1, 200000)
atm_2 = ATM('A02', bank2, 300000)

manage_task.create_atm(atm_1)
manage_task.create_atm(atm_2)

manage_task.main_menu()