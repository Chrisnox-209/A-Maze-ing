import time

class Timer:
    def __init__(self):
        self.start = time.perf_counter()
 
    def restart(self):
        self.start = time.perf_counter()
 
    def get_time(self):
        return time.perf_counter() - self.start

timeer = Timer()
timestr = f"{timeer.get_time(): .0f}"
print(f"Programme exécuté en : {timestr} secondes")

