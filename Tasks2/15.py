from pathlib import Path
def count_lines(stream):
    return sum(1 for line in stream)


base = Path(__file__).resolve().parent
from io import StringIO
with open(base / "data.txt", encoding="utf-8") as file:
    print("Файл:", count_lines(file))
print("StringIO:", count_lines(StringIO("first\nsecond\nthird")))
