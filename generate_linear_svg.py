from linear_search import linear_search

dataset = list(range(1000000))
target = 9999999  # Missing element (worst case) to trigger full scans

# Loop to generate enough execution samples for py-spy
for _ in range(3000):
    linear_search(dataset, target)