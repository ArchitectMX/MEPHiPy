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
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} deposit failed: invalid amount {money}")
            raise ValueError("amount must be positive")

        self._balance += money
        self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} deposit: {money}")

    def withdraw(self, money):
        if money <= 0:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: invalid amount {money}")
            raise ValueError("amount must be positive")

        if money > self._balance:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: insufficient funds ({money})")
            raise ValueError("insufficient funds")

        self._balance -= money
        self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal: {money}")

    def get_balance(self):
        return self._balance

    def get_history(self):
        return self._log


class SavingAccount(BankAccount):
    def __init__(self, user, log):
        super().__init__(user, log)
        self._savingLimit = 1000

    @property
    def savingLimit(self):
        return self._savingLimit

    def withdraw(self, money):
        if money <= 0:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: invalid amount {money}")
            raise ValueError("amount must be positive")

        if money + self._savingLimit > self._balance:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: insufficient funds ({money})")
            raise ValueError("insufficient funds")

        self._balance -= money
        self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal: {money}")


class CreditAccount(BankAccount):
    def __init__(self, user, log):
        super().__init__(user, log)
        self._creditLimit = 10000

    @property
    def creditLimit(self):
        return self._creditLimit

    def withdraw(self, money):
        if money <= 0:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: invalid amount {money}")
            raise ValueError("amount must be positive")

        if money - self._creditLimit > self._balance:
            self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal failed: insufficient funds ({money})")
            raise ValueError("insufficient funds")

        self._balance -= money
        self._log.append(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} withdrawal: {money}")


newAcc = BankAccount("Name")
newAcc.deposit(1000)
newAcc.deposit(-100)
newAcc.withdraw(900)
newAcc.withdraw(900)
newAcc.withdraw(-900)
print(newAcc.get_balance())
print(newAcc.get_history())

