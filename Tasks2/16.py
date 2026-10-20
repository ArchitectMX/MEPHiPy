from pathlib import Path
import re


def analyze_logs(path):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    error_users = set()
    pattern = re.compile(r"\b(INFO|WARNING|ERROR)\s+User\s+(\d+)\b")
    with open(path, encoding="utf-8") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                level, user = match.groups()
                counts[level] += 1
                if level == "ERROR":
                    error_users.add(user)
    return counts, sorted(error_users)


base = Path(__file__).resolve().parent
try:
    counts, users = analyze_logs(base / "dated.log")
    for level in ("INFO", "WARNING", "ERROR"):
        print(f"{level}: {counts[level]}")
    print("Пользователи с ошибками:", users)
except (OSError, UnicodeError) as error:
    print("Ошибка чтения:", error)
