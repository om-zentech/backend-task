from controller.atm_controller import ATMController

class ATMView:

    def __init__(self):
        self.controller = ATMController()

    def run(self):

        while True:

            print("\n----- ATM SYSTEM -----")
            print("1. Register")
            print("2. Create ATM")
            print("3. Login")
            print("4. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":

                name = input("Name: ").strip()
                
                if not name:
                    print("Name cannot be empty!")
                    continue

                bank = input("Bank: ").strip()
                
                if not bank:
                    
                    print("Bank name cannot be empty!")
                    continue

                try:
                    
                    balance = float(input("Balance: "))
                    if balance < 0:
                        
                        print("Balance cannot be negative!")
                        continue
                except ValueError:
                    
                    print("Invalid balance amount!")
                    continue

                result = self.controller.create_user(name, bank, balance)

                if result["success"]:
                    
                    print("\nUser Created Successfully")
                    print("Card:", result["card"])
                    print("PIN:", result["pin"])
                    
                else:
                    
                    print(result["message"])

            elif choice == "2":

                atm_id = input("ATM ID: ").strip()
                
                if not atm_id:
                    
                    print("ATM ID cannot be empty!")
                    
                    continue

                bank = input("Bank: ").strip()
                
                if not bank:
                    
                    print("Bank name cannot be empty!")
                    continue

                try:
                    
                    balance = float(input("ATM Balance: "))
                    
                    if balance < 0:
                        
                        print("ATM balance cannot be negative!")
                        continue
                    
                except ValueError:
                    
                    print("Invalid ATM balance!")
                    continue

                result = self.controller.create_atm(atm_id, bank, balance)

                print(result["message"])

            elif choice == "3":

                card = input("Card Number: ").strip()
                
                if not card.isdigit() or len(card) != 16:
                    
                    print("Card number must be 16 digits!")
                    continue

                pin = input("PIN: ").strip()
                
                if not pin.isdigit() or len(pin) != 4:
                    
                    print("PIN must be 4 digits!")
                    continue

                result = self.controller.login(card, pin)

                if not result["success"]:
                    
                    print("\nInvalid Credentials!")
                    continue

                user = result["data"]

                while True:

                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Show Balance")
                    print("4. Show Account Details")
                    print("5. Logout")

                    op = input("Enter Choice: ").strip()

                    if op == "1":

                        try:
                            amount = float(input("\nEnter Deposit Amount: "))
                            if amount <= 0:
                                print("Deposit must be greater than 0!")
                                continue
                        except ValueError:
                            print("Invalid deposit amount!")
                            continue

                        result = self.controller.deposit(user[0], amount)

                        print(result["message"])

                    elif op == "2":

                        try:
                            amount = float(input("Enter Withdraw Amount: "))
                            if amount <= 0:
                                print("Withdraw amount must be greater than 0!")
                                continue
                        except ValueError:
                            print("Invalid withdraw amount!")
                            continue

                        atm_id = input("Enter ATM ID: ").strip()

                        if not atm_id:
                            print("ATM ID cannot be empty!")
                            continue

                        result = self.controller.withdraw(user, amount, atm_id)

                        print(result["message"])

                    elif op == "3":

                        result = self.controller.show_balance(user[0])

                        if result["success"]:
                            print("\n----- Current Balance -----")
                            print("Available Balance:", result["balance"])
                        else:
                            print(result["message"])

                    elif op == "4":

                        result = self.controller.show_account_details(user[0])

                        if result["success"]:
                            user_data = result["data"]

                            print("\n----- Account Details -----")
                            print("Name:", user_data[0])
                            print("Card Number:", user_data[1])
                            print("Bank:", user_data[5])
                            print("Balance:", user_data[2])
                            print("Transaction Count:", user_data[3])
                            print("Total Withdrawal Today:", user_data[4])
                        else:
                            print(result["message"])

                    elif op == "5":
                        print("\nLogged out successfully!")
                        break

                    else:
                        print("\nInvalid Option!")

            elif choice == "4":

                print("\nExiting...")
                break

            else:
                print("\nInvalid Choice!")