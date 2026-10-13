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


if __name__ == "__main__":
    try:
        balance = float(input("Текущий баланс: "))
        amount = float(input("Сумма снятия: "))
        print(f"Новый баланс: {withdraw(balance, amount):.2f}")
    except BankError as error:
        print(f"Ошибка: {error}")
    except ValueError:
        print("Ошибка: введите числа")
