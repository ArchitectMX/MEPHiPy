from pathlib import Path
import re


def analyze_logs(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    user_ids = re.findall(r"\bUser\s+(\d+)\b", "\n".join(lines))
    error_lines = [line for line in lines if re.search(r"\bERROR\b", line)]
    error_user_ids = []

    for line in error_lines:
        match = re.search(r"\bUser\s+(\d+)\b", line)
        if match:
            error_user_ids.append(match.group(1))

    return user_ids, error_lines, error_user_ids


base = Path(__file__).resolve().parent
try:
    users, errors, error_users = analyze_logs(base / "users.log")
    print("Все пользователи:", users)
    print("Строки с ERROR:", *errors, sep="\n")
    print("Пользователи с ошибками:", error_users)
except (OSError, UnicodeError) as error:
    print("Ошибка чтения:", error)
