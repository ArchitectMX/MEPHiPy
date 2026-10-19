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

    for item in sorted(path.iterdir()):
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            directories.append(item)

    for item in sorted(path.rglob("*")):
        if item.is_file():
            total_size += item.stat().st_size
            if item.suffix == ".py":
                python_files.append(item)

    return len(files), len(directories), python_files, total_size


base = Path(__file__).resolve().parent
try:
    print(analyze_directory(input("Каталог (Enter — текущий): ") or base))
except OSError as error:
    print(error)
