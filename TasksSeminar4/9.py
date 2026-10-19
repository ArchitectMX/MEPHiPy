def parse_number(value):
    return float(value)


try:
    print(parse_number(input("Введите число: ")))
except ValueError:
    print("Некорректное число")
