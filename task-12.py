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
  def __init__(self,name,bank_name,balance):
    self.name = name
    self.bank_name = bank_name
    self.balance = balance
    self.card_number = str(random.randint(10**15,(10**16)-1))
    self.pin_number = str(random.randint(1000,9999))
    self.count_of_transaction = 0
    self.total_withdrawal = 0  

class Bank:
  def __init__(self,bank_name):
    self.bank_name = bank_name

class ATM:
  def __init__(self,id,bank_name,initial_balance):
    self.id = id
    self.bank_name = bank_name
    self.initial_balance = initial_balance
    self.per_transaction_limit = 10000
    self.daily_transaction_limit = 25000
    self.no_of_transaction_per_day = 3

class DictManagement:
  def __init__(self):
    self.atms = {}
    self.banks = []
    self.users = {}
  
  def create_user(self,user_data):
    self.users[user_data.card_number] = user_data
    self.banks.append(user_data.bank_name)
    print(f'\n----- User Created -----\nName: {user_data.name}\nBank: {user_data.bank_name}\nCard Number: {user_data.card_number}\nPin: {user_data.pin_number}\nBalance: {user_data.balance}\n')

  def create_atm(self,atm_data):
    self.atms[atm_data.id] = atm_data
    print(f'\n-----ATM Created-----\nID: {atm_data.id}\nBank: {atm_data.bank_name}\nATM Balance: {atm_data.initial_balance}\n')
  
  def create_user_input(self):
    while True:
      try:
        name = input('Enter User Name: ')
        bank_name = input('Enter Bank Name: ')
        balance = float(input('Enter Balance: '))
        if balance < 0:
          print('Balance cannot be negative, try again!')
          continue
        user_data = User(name,bank_name,balance)
        self.create_user(user_data)
        break
      except ValueError:
        print('Invalid Input, try again!')

  def update_user(self,user_data,atm_data):
    while True:
      try:
        print('\n-----Select Detail to Update-----\n1.Name\n2.Bank Name\n3.Pin\n4.Exit\n')
        input_choice = input('Enter Choice: ')
        if input_choice == '1':
          new_name = input('Enter new name: ')
          user_data.name = new_name
          print(f'\n----- User Details Updated -----\nName: {user_data.name}\nBank: {user_data.bank_name}\nCard Number: {user_data.card_number}\nPin: {user_data.pin_number}\nBalance: {user_data.balance}\n')
        elif input_choice == '2':
          new_bank_name = input('Enter new bank name: ')
          user_data.bank_name = new_bank_name
          print(f'\n----- User Details Updated -----\nName: {user_data.name}\nBank: {user_data.bank_name}\nCard Number: {user_data.card_number}\nPin: {user_data.pin_number}\nBalance: {user_data.balance}\n')
        elif input_choice == '3':
          new_pin = str(random.randint(1000,9999))
          user_data.pin_number = new_pin
          print(f'\n----- User Details Updated -----\nName: {user_data.name}\nBank: {user_data.bank_name}\nCard Number: {user_data.card_number}\nPin: {user_data.pin_number}\nBalance: {user_data.balance}\n')
        elif input_choice == '4':
          break
        else:
          print('Invalid Input, try again!')
      except ValueError:
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
      try:
        input_card_number = input('Enter Card Number: ')
        input_pin_number = input('Enter Pin: ')
        if input_card_number not in self.users:
          print('\nUser with this Card number not exist, try again!\n')
          continue
        elif self.users[input_card_number].pin_number != input_pin_number:
          print('\nIncorrect pin, try again!\n')
          continue
        else:
          break
      except ValueError:
        print('\nInvalid Input, try again!')

    user_data = self.users.get(input_card_number)
    atm_data = self.atms[input_atm_id]
    while True:
      print('\n-----Select Operation-----\n1.Deposite\n2.Withdraw\n3.Check bank balance\n4.Get account details\n5.Update your details\n6.Exit')
      input_choice = input('\nEnter Choice: ')
      if input_choice == '1':
        self.deposite(user_data,atm_data)
      elif input_choice == '2':
        self.withdrawal(user_data,atm_data)
      elif input_choice == '3':
        print(f'\n-----Bank Balance-----\nAvailable Balance: {user_data.balance}\n')
      elif input_choice == '4':
        print(f'\n-----Account Details-----\nName: {user_data.name}\nBank: {user_data.bank_name}\nCard Number: {user_data.card_number}\nPin: {user_data.pin_number}\nBalance: {user_data.balance}\n')
      elif input_choice == '5':
        self.update_user(user_data,atm_data)
      elif input_choice == '6':
        break
      else:
        print('Invalid Input, try again!')
  
  def deposite(self,user_data,atm_data):
    data = self.users.get(user_data.card_number)
    atm_data = self.atms[atm_data.id]
    deposite_amount = float(input('\nEnter amount to be deposite: '))
    data.balance += deposite_amount
    atm_data.initial_balance += deposite_amount
    print(f'\n----- Money Successfuly Deposited to your account -----\nName: {data.name}\nBank: {data.bank_name}\nCard Number: {data.card_number}\nBalance: {data.balance}\n')

  def withdrawal(self,user_data,atm_data):
    data = self.users.get(user_data.card_number)
    atm_data = self.atms[atm_data.id]
    withdrawal_amount = float(input('\nEnter amount to be withdrawal: '))

    if data.count_of_transaction >= atm_data.no_of_transaction_per_day:
      print('\nTransaction limit reached for today!')
    elif withdrawal_amount > atm_data.per_transaction_limit:
      print('\nYou can Withdraw only 10000 per transaction!')
    elif atm_data.initial_balance < withdrawal_amount:
      print('\nInsufficient balance in ATM')
    elif withdrawal_amount > data.balance:
      print('\nInsufficient money for withdraw')
    elif data.total_withdrawal > atm_data.daily_transaction_limit:
      print('\nWithdrawal limit reached for today!')
    elif user_data.bank_name == atm_data.bank_name:
      data.balance -= withdrawal_amount
      atm_data.initial_balance -= withdrawal_amount
      data.count_of_transaction += 1
      data.total_withdrawal += withdrawal_amount
      print(f'\n----- Money Successfuly Withdraw from your account -----\nName: {data.name}\nBank: {data.bank_name}\nCard Number: {data.card_number}\nBalance: {data.balance}\n') 
    else:
      data.balance -= withdrawal_amount + (withdrawal_amount * 0.05)
      atm_data.initial_balance -= withdrawal_amount + (withdrawal_amount * 0.05)
      data.count_of_transaction += 1
      data.total_withdrawal += withdrawal_amount + (withdrawal_amount * 0.05)
      print(f'\n----- Money Successfuly Withdraw from your account -----\nName: {data.name}\nBank: {data.bank_name}\nCard Number: {data.card_number}\nBalance: {data.balance}\n') 
      print('\n5% transaction fees applied\n')

dict_manage = DictManagement()
atm_1 = ATM('A01','BOB',200000)
atm_2 = ATM('A02','HDFC',300000)
dict_manage.create_atm(atm_1)
dict_manage.create_atm(atm_2)
dict_manage.main_menu()