from binary_search import binary_search

dataset = list(range(1000000))
target = 9999999  # Missing element (worst case)

# High iteration count so py-spy captures logarithmic execution steps
for _ in range(500000):
    binary_search(dataset, target)