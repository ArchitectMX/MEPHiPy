import time
from contextlib import contextmanager


class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        elapsed_time = time.perf_counter() - self.start_time
        self.elapsed = elapsed_time
        print(f"Время выполнения: {elapsed_time:.6f} секунд")
        return False


@contextmanager
def timer():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        elapsed_time = time.perf_counter() - start_time
        print(f"Время выполнения: {elapsed_time:.6f} секунд")


def some_function():
    return sum(range(1_000_000))


with Timer():
    print(some_function())
with timer():
    print(some_function())
