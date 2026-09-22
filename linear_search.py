import time


def linear_search(arr, target):
    """Linear Search: Iterates through array sequentially to find target.

    Time Complexity:
        - Best Case: O(1)
        - Average Case: O(n)
        - Worst Case: O(n)
    Space Complexity: O(1)
    """
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons  # Returns index and total comparisons
    return -1, comparisons  # Returns -1 if target is not found


if __name__ == "__main__":
    DATA_SIZE = 1000000
    dataset = list(range(DATA_SIZE))
    target = 9999999  # Worst case target

    t0 = time.perf_counter()
    index, comps = linear_search(dataset, target)
    elapsed_time = (time.perf_counter() - t0) * 1000  # Convert to ms

    print("--- Linear Search Demonstration ---")
    print(f"Dataset Size:     {DATA_SIZE:,}")
    print(f"Target Found:     {index != -1}")
    print(f"Comparisons Made: {comps:,}")
    print(f"Execution Time:   {elapsed_time:.6f} ms")