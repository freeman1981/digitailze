from concurrent.futures import ThreadPoolExecutor
import time


def work():
    for _ in range(100_000_000):
        pass


start = time.time()

with ThreadPoolExecutor(max_workers=4) as e:
    e.submit(work)
    e.submit(work)
    e.submit(work)
    e.submit(work)

print(time.time() - start)
