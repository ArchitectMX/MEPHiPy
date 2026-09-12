class BankAccount:
    def __init__(self, user):
        self.user = user
        self._balance = 0
        self._log = []

    @property
    def balance(self):
        return self._balance

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def get_balance(self):
        return self._balance

    def get_history(self):
        pass


class SavingAccount(BankAccount):
    def __init__(self, user, log):
        super().__init__(user, log)


class CreditAccount(BankAccount):
    def __init__(self, user, log):
        super().__init__(user, log)
