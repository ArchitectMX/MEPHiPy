from pathlib import Path
from contextlib import contextmanager


@contextmanager
def log_operation(path, operation):
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"START: {operation}\n")
        file.flush()
        try:
            yield
        except BaseException:
            file.write(f"ERROR: {operation}\n")
            raise
        else:
            file.write(f"END: {operation}\n")


base = Path(__file__).resolve().parent
with log_operation(base / "operation.log", "Data processing"):
    print("Обработка данных")
