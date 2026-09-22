import time
from binary_search import binary_search

# Large sorted array
data = list(range(1000000))
target = 999999

# Run 500,000 iterations to ensure long execution and high sample count
start_time = time.perf_counter()
for _ in range(500000):
    binary_search(data, target)
end_time = time.perf_counter()

total_time_ms = (end_time - start_time) * 1000
print(f"Total execution time: {total_time_ms:.4f} ms")
print(f"Average Binary Search time per call: {total_time_ms / 500000:.6f} ms")