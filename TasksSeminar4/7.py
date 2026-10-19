from pathlib import Path


def find_files(directory, extension):
    path = Path(directory)
    if not path.is_dir():
        raise NotADirectoryError(f"Каталог не найден: {path}")
    extension = "." + extension.lstrip(".")
    for item in sorted(path.rglob("*")):
        if item.is_file() and item.suffix == extension:
            yield item, item.stat().st_size


base = Path(__file__).resolve().parent
try:
    directory = input("Каталог (Enter — текущий): ") or base
    extension = input("Расширение (Enter — .py): ") or ".py"
    for path, size in find_files(directory, extension):
        print(path, size, "байт")
except OSError as error:
    print(error)
