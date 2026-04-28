import time


class Timer:
    def __init__(self) -> None:
        self.start: float = time.perf_counter()

    def restart(self) -> None:
        self.start = time.perf_counter()

    def get_time(self) -> float:
        return time.perf_counter() - self.start
