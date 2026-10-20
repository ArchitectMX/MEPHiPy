import csv
from pathlib import Path


base = Path(__file__).resolve().parent

with open(base / "products.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    lst = []
    for i in reader:
        if float(i["price"]) > 100:
            lst.append(i)

with open(base / "expensive.csv", "w", encoding="utf-8", newline="") as nf:
    writer = csv.DictWriter(nf, fieldnames=fields)
    writer.writeheader()
    writer.writerows(lst)

print("Создан expensive.csv")
