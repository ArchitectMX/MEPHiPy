from pathlib import Path
def number_statistics(path):
    total = count = 0
    minimum = maximum = None
    with open(path, encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            try:
                number = int(line)
            except ValueError:
                print(f"Строка {line_number}: пропущено неверное число")
                continue
            total += number
            count += 1
            minimum = number if minimum is None else min(minimum, number)
            maximum = number if maximum is None else max(maximum, number)
    return {"minimum": minimum, "maximum": maximum, "average": total / count if count else None}


base = Path(__file__).resolve().parent
result = number_statistics(base / "numbers.txt")
(base / "result.txt").write_text("\n".join(f"{key}: {value}" for key, value in result.items()) + "\n", encoding="utf-8")
print(result)
