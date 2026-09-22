"""
Linear Search Execution Time Measurement (Seconds)
Course: 02AML204 – Introduction to Artificial Intelligence
PRN: 25UAM004
Name: Siddhi Sachin Patil
"""

import time


def linear_search(arr, target):
    """
    Linear Search: Iterates sequentially through the array.
    Time Complexity: Best O(1), Avg/Worst O(n)
    """
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


if __name__ == "__main__":
    DATA_SIZE = 1_000_000
    dataset = list(range(DATA_SIZE))

    # Test cases
    cases = {
        "Best Case (Target = 0)": 0,
        "Average Case (Target = 404,310)": 404310,
        "Worst Case (Target = 9,999,999)": 9_999_999,
    }

    print("==================================================")
    print(f" LINEAR SEARCH EXECUTION TIME (N = {DATA_SIZE:,})")
    print("==================================================\n")

    for case_name, target in cases.items():
        start_time = time.perf_counter()
        index, comparisons = linear_search(dataset, target)
        end_time = time.perf_counter()

        elapsed_time_sec = end_time - start_time  # Time in seconds

        print(f"--- {case_name} ---")
        print(f"Target Value:     {target}")
        print(f"Index Returned:   {index}")
        print(f"Comparisons Made: {comparisons:,}")
        print(f"Execution Time:   {elapsed_time_sec:.8f} sec\n")