#Exercise 1: Bank Account
#PART1
import sys

# ====== PART 1 & 2: Bank Accounts ======
class BankAccount:
    def __init__(self, balance=0, username="", password=""):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"\n{username} successfully authenticated!\n")
        else:
            self.authenticated = False
            print("\nAuthentication failed.\n")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to deposit.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, username="", password="", minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Balance cannot go below minimum ({self.minimum_balance}).")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# ====== PART 3 & 4: ATM ======
class ATM:
    def __init__(self, account_list, try_limit=3):
        if not isinstance(account_list, list):
            raise Exception("account_list must be a list of accounts.")
        for acc in account_list:
            if not isinstance(acc, (BankAccount, MinimumBalanceAccount)):
                raise Exception("All items in account_list must be BankAccount or MinimumBalanceAccount instances.")
        if try_limit <= 0:
            print("Invalid try_limit, defaulting to 3.")
            try_limit = 3

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.prompt_login()
            elif choice == "2":
                print("Exiting ATM...")
                sys.exit()
            else:
                print("Invalid choice. Try again.")

    def prompt_login(self):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        self.log_in(username, password)

    def log_in(self, username, password):
        for acc in self.account_list:
            if acc.username == username:
                acc.authenticate(username, password)
                if acc.authenticated:
                    self.show_account_menu(acc)
                    return

        self.current_tries += 1
        print(f"Incorrect login. Attempt {self.current_tries}/{self.try_limit}")
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            sys.exit()
        else:
            self.prompt_login()

    def show_account_menu(self, account):
        while True:
            print("\n--- Account Menu ---")
            print(f"Current balance: {account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Logout")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                try:
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid number.")
                except Exception as e:
                    print(e)
            elif choice == "2":
                try:
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number.")
                except Exception as e:
                    print(e)
            elif choice == "3":
                print(f"{account.username} logged out.\n")
                account.authenticated = False
                break
            else:
                print("Invalid choice. Try again.")


# ====== Example Usage ======
if __name__ == "__main__":
    acc1 = BankAccount(balance=100, username="eraji", password="951847")
    acc2 = MinimumBalanceAccount(balance=200, username="Eraji", password="abcd", minimum_balance=50)

    atm_machine = ATM([acc1, acc2], try_limit=3)
    atm_machine.show_main_menu()
