import time
from linear_search import linear_search

data = list(range(1000000))
target = 999999

start_time = time.perf_counter()
for _ in range(10):
    linear_search(data, target)
end_time = time.perf_counter()

avg_time_ms = ((end_time - start_time) / 10) * 1000
print(f"Total loop time: {end_time - start_time:.4f} s")
print(f"Average Linear Search time per call: {avg_time_ms:.6f} ms")