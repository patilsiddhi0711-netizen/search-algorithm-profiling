import time


def binary_search(arr, target):
    """Binary Search: Repeatedly divides search space in half.
    Note: Requires a sorted array.

    Time Complexity:
        - Best Case: O(1)
        - Average Case: O(log n)
        - Worst Case: O(log n)
    Space Complexity: O(1)
    """
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons  # Returns index and total comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons  # Returns -1 if target is not found


if __name__ == "__main__":
    DATA_SIZE = 1000000
    dataset = list(range(DATA_SIZE))  # Sorted list
    target = 9999999  # Worst case target

    t0 = time.perf_counter()
    index, comps = binary_search(dataset, target)
    elapsed_time = (time.perf_counter() - t0) * 1000  # Convert to ms

    print("--- Binary Search Demonstration ---")
    print(f"Dataset Size:     {DATA_SIZE:,}")
    print(f"Target Found:     {index != -1}")
    print(f"Comparisons Made: {comps:,}")
    print(f"Execution Time:   {elapsed_time:.6f} ms")