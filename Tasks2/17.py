from pathlib import Path
def analyze_numbers(path):
    total = count = 0
    minimum = maximum = None
    with open(path, encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            try:
                number = int(line)
            except ValueError:
                raise ValueError(f"Строка {line_number}: ожидалось целое число") from None
            count += 1
            total += number
            minimum = number if minimum is None else min(minimum, number)
            maximum = number if maximum is None else max(maximum, number)
    return {"sum": total, "minimum": minimum, "maximum": maximum,
            "count": count, "average": total / count if count else None}


base = Path(__file__).resolve().parent
try:
    print(analyze_numbers(base / "numbers_large.txt"))
except (OSError, ValueError) as error:
    print(error)
