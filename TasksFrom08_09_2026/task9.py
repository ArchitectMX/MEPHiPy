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


class CreditAccount(BankAccount):
    def __init__(self, user, log):
        super().__init__(user, log)
