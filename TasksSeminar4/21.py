import re


def is_valid_login(login):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{3,15}", login) is not None


for login in ["user_123", "admin", "123user", "ab", "user-name", "very_long_username"]:
    print(login, is_valid_login(login))
