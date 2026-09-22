"""
Binary Search Execution Time Measurement (Seconds)
Course: 02AML204 – Introduction to Artificial Intelligence
PRN: 25UAM004
Name: Siddhi Sachin Patil
"""

import time


def binary_search(arr, target):
    """
    Binary Search: Repeatedly divides search space in half.
    Time Complexity: Best O(1), Avg/Worst O(log n)
    """
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


if __name__ == "__main__":
    DATA_SIZE = 1_000_000
    dataset = list(range(DATA_SIZE))

    # Test cases
    cases = {
        "Best Case (Midpoint Target)": dataset[(DATA_SIZE // 2) - 1],  # 499,999
        "Average Case (Target = 404,310)": 404310,
        "Worst Case (Target = 9,999,999)": 9_999_999,
    }

    print("==================================================")
    print(f" BINARY SEARCH EXECUTION TIME (N = {DATA_SIZE:,})")
    print("==================================================\n")

    for case_name, target in cases.items():
        # Running batch iterations for stable sub-millisecond precision
        iterations = 1000
        start_time = time.perf_counter()
        for _ in range(iterations):
            index, comparisons = binary_search(dataset, target)
        end_time = time.perf_counter()

        # Average elapsed time per call in seconds
        elapsed_time_sec = (end_time - start_time) / iterations

        print(f"--- {case_name} ---")
        print(f"Target Value:     {target}")
        print(f"Index Returned:   {index}")
        print(f"Comparisons Made: {comparisons}")
        print(f"Execution Time:   {elapsed_time_sec:.8f} sec\n")