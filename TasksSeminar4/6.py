from pathlib import Path


def analyze_directory(directory):
    path = Path(directory)
    if not path.exists():
        raise FileNotFoundError(f"Каталог не найден: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"Указанный путь не является каталогом: {path}")

    files = []
    directories = []
    python_files = []
    total_size = 0

    for item in path.iterdir():
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            directories.append(item)

    for item in path.rglob("*"):
        if item.is_file():
            total_size += item.stat().st_size
            if item.suffix == ".py":
                python_files.append(item)

    return len(files), len(directories), python_files, total_size


if __name__ == "__main__":
    directory = input("Введите путь к каталогу: ")
    try:
        file_count, directory_count, python_files, total_size = analyze_directory(directory)
        print(f"Количество файлов: {file_count}")
        print(f"Количество подкаталогов: {directory_count}")
        print("Python-файлы:")
        if python_files:
            for file in python_files:
                print(file)
        else:
            print("не найдены")
        print(f"Суммарный размер всех файлов: {total_size} байт")
    except (FileNotFoundError, NotADirectoryError, PermissionError, OSError) as error:
        print(f"Ошибка: {error}")
