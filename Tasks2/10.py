class BankError(Exception):
    """Базовое исключение для операций с банковским счётом."""


class InvalidAmountError(BankError):
    """Сумма снятия отрицательная или равна нулю."""


class InsufficientFundsError(BankError):
    """На счёте недостаточно денег."""


class AccountBlockedError(BankError):
    """Счёт заблокирован."""


def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма снятия должна быть больше нуля")
    if amount > balance:
        raise InsufficientFundsError("На счёте недостаточно денег")
    return balance - amount


try:
    balance = float(input("Баланс: "))
    amount = float(input("Сумма снятия: "))
    print("Новый баланс:", withdraw(balance, amount))
except (BankError, ValueError) as error:
    print("Ошибка:", error)
