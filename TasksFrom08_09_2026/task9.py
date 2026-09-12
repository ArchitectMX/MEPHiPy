from datetime import datetime


class BankAccount:
    def __init__(self, user):
        self.user = user
        self._balance = 0
        self._log = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        if money <= 0:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} deposit failed: invalid amount: {money}")
            return ValueError("amount must be positive")

        self._balance += money
        self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} deposit: {money}")

    def withdraw(self, money):
        if money <= 0:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: invalid amount: {money}")
            return ValueError("amount must be positive")

        if money > self._balance:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: insufficient funds: {money}")
            return ValueError("insufficient funds")

        self._balance -= money
        self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal: {money}")

    def get_balance(self):
        return self._balance

    def get_history(self):
        return self._log


class SavingsAccount(BankAccount):
    def __init__(self, user):
        super().__init__(user)
        self._savingLimit = 1000

    @property
    def savingLimit(self):
        return self._savingLimit

    def withdraw(self, money):
        if money <= 0:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: invalid amount: {money}")
            return ValueError("amount must be positive")

        if money + self._savingLimit > self._balance:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: insufficient funds: {money}")
            return ValueError("insufficient funds")

        self._balance -= money
        self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal: {money}")


class CreditAccount(BankAccount):
    def __init__(self, user):
        super().__init__(user)
        self._creditLimit = 10000

    @property
    def creditLimit(self):
        return self._creditLimit

    def withdraw(self, money):
        if money <= 0:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: invalid amount: {money}")
            return ValueError("amount must be positive")

        if money - self._creditLimit > self._balance:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: insufficient funds: {money}")
            return ValueError("insufficient funds")

        self._balance -= money
        self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal: {money}")


accounts = [
    BankAccount("Base"),
    SavingsAccount("Saving"),
    CreditAccount("Credit")
]

for account in accounts:
    account.deposit(5000)

for account in accounts:
    account.withdraw(6000)

for account in accounts:
    print(type(account).__name__)
    print("balance:", account.get_balance())
    print("history:", account.get_history())
    print()