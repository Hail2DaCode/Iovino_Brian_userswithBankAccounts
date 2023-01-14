class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount, repeat = 1):
    	self.account.deposit(amount, repeat)
    def make_withdrawal(self, amount, repeat = 1):
        self.account.withdraw(amount, repeat)
    def display_user_balance(self):
        self.account.display_account_info()


class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance = 0,):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
    def deposit(self, amount, repeat = 1):
        self.balance += amount * repeat
        return self
    def withdraw(self, amount, repeat = 1):
        if self.balance >= amount * repeat:
            self.balance -= amount * repeat
        else:
            print("Insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(self.balance)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    @classmethod
    def info_for_all_accounts(cls):
        for account in BankAccount.all_accounts:
            account.display_account_info()

user_1 = User("Brian", "iovinob2@gmail.com")
print(user_1.name)
user_1.account.display_account_info()
print(user_1.account.int_rate)
user_1.make_deposit(1500)
user_1.account.display_account_info()
user_1.make_withdrawal(100, 10)
user_1.account.display_account_info()
user_1.display_user_balance()