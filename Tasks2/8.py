from pathlib import Path
def read_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Нет прав на чтение файла")
    except IsADirectoryError:
        print("Указан каталог вместо файла")
    except UnicodeError:
        print("Не удалось прочитать файл в кодировке UTF-8")
    except OSError as error:
        print(f"Ошибка операционной системы: {error}")
    return None


base = Path(__file__).resolve().parent
content = read_file(input("Файл (Enter — data.txt): ") or base / "data.txt")
if content is not None:
    print(content)
