import csv
from pathlib import Path


base = Path(__file__).resolve().parent
groups = {}
total = 0
count = 0
maxScore = -float("inf")
name = ""

with open(base / "students.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i in reader:
        score = int(i["score"])
        group = i["group"]
        total += score
        count += 1
        if score > maxScore:
            maxScore = score
            name = i["name"]
        if group not in groups:
            groups[group] = []
        groups[group].append(score)

if count:
    print("Средний балл:", total / count)
    print("Лучший студент:", name, maxScore)
    for group, scores in groups.items():
        print(group, sum(scores) / len(scores))
else:
    print("В файле нет студентов")
