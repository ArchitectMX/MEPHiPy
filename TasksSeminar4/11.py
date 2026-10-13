import re


def analyze_logs(file_path):
    with open(file_path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file]

    user_ids = re.findall(r"\bUser\s+(\d+)\b", "\n".join(lines))
    error_lines = [line for line in lines if re.search(r"\bERROR\b", line)]
    error_user_ids = []

    for line in error_lines:
        match = re.search(r"\bUser\s+(\d+)\b", line)
        if match:
            error_user_ids.append(match.group(1))

    return user_ids, error_lines, error_user_ids


if __name__ == "__main__":
    path = input("Введите путь к файлу с логами: ")
    try:
        users, errors, error_users = analyze_logs(path)
        print("Все идентификаторы пользователей:", users)
        print("Строки с ERROR:")
        for error in errors:
            print(error)
        print("Идентификаторы пользователей с ошибками:", error_users)
    except (FileNotFoundError, PermissionError, OSError) as error:
        print(f"Ошибка чтения файла: {error}")
