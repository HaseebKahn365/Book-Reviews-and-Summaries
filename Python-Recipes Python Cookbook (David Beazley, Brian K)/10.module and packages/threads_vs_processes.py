import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def heavy_math(n):
    return n * n

if __name__ == "__main__":
    numbers = range(1, 1001)

    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(heavy_math, numbers))
    print(f"Threads took: {time.time() - start:.4f}s")

    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(heavy_math, numbers))
    print(f"Processes took: {time.time() - start:.4f}s")