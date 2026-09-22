# Search Algorithm Profiling: Linear Search vs. Binary Search

An empirical CPU profiling and computational performance analysis comparing **Linear Search ($O(n)$)** and **Binary Search ($O(\log n)$)** using Python's `time.perf_counter()` and non-intrusive CPython stack profiling via `py-spy`.

---

## 📌 Project Overview

Searching algorithms are fundamental building blocks in computer science. While theoretical time complexity gives an asymptotic bound on performance, real-world execution depends heavily on hardware interaction, memory layout, call stack overhead, and implementation efficiency.

This repository provides:
1. Pure Python implementations of Linear Search and Binary Search on sorted arrays containing **1,000,000 elements**.
2. High-precision execution timing using Python's `time.perf_counter()`.
3. CPU call stack flamegraphs generated via `py-spy` to inspect stack depth, sample frequency, and computational hot spots during execution.

---

## 💡 Algorithmic Analysis & Complexity

### 1. Linear Search
* **Algorithm:** Iterates sequentially through each element in the dataset from index `0` to `n-1` until the target element is located or the array ends.
* **Best Case Complexity:** $O(1)$ (target is at index `0`).
* **Worst/Average Case Complexity:** $O(n)$ (target is at index `n-1` or not present).
* **Space Complexity:** $O(1)$ auxiliary space.

### 2. Binary Search
* **Algorithm:** Operates on pre-sorted arrays using a divide-and-conquer approach. It repeatedly divides the search interval in half by comparing the target element with the middle element.
* **Best Case Complexity:** $O(1)$ (target is exactly at the middle index).
* **Worst/Average Case Complexity:** $O(\log_2 n)$ (target requires maximum interval divisions).
* **Space Complexity:** $O(1)$ auxiliary space for iterative implementations.

---

## 📊 Empirical Performance & Profiling Results

Profiling was conducted on a dataset of size $N = 1,000,000$ searching for the worst-case target (`999999`). Sampling was executed at 100 Hz (100 samples/sec) using `py-spy`.

| Metric | Linear Search | Binary Search |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | $O(\log n)$ |
| **Comparisons Required (Worst Case)** | $1,000,000$ | $\approx \log_2(1,000,000) \approx 20$ |
| **Execution Speed Per Search** | $\approx 157.85\text{ ms}$–$245.41\text{ ms}$ | $\approx 0.0088\text{ ms}$–$0.0151\text{ ms}$ |
| **Total Test Batch Execution Time** | $\approx 2.45\text{ seconds}$ (10 calls) | $\approx 4.41\text{ seconds}$ (500,000 calls) |
| **`py-spy` Samples Captured** | $266\text{ samples}$ | $451\text{ samples}$ |
| **Profiling Artifact** | `images/linear_search_flamegraph.svg` | `images/binary_search_flamegraph.svg` |

### Key Observations:
* **Asymptotic Efficiency:** Binary search performs $\approx 10,000\times$ to $20,000\times$ faster per call than linear search on $1,000,000$ items.
* **CPU Sampling:** Due to Binary Search executing in nanoseconds, running single iterations yields insufficient sampling data for profilers. Profiling required batch looping ($500,000$ iterations) to allow `py-spy` to capture hundreds of valid CPU samples ($451$ samples across $4.41\text{ seconds}$).

---

## 🖼️ Flamegraph Visualizations

The generated interactive SVG flamegraphs provide visual proof of CPU time spent inside each function frame:

1. **Linear Search Flamegraph (`images/linear_search_flamegraph.svg`)**:
   * Shows a wide base stack frame corresponding to index traversal loop overhead and list item comparison.
2. **Binary Search Flamegraph (`images/binary_search_flamegraph.svg`)**:
   * Captures high-frequency loop executions, displaying stack frames where midpoint calculation (`(low + high) // 2`) and bounds adjusting occur.

*Note: View the full interactive SVG files inside the `images/` directory by opening them in Google Chrome, Microsoft Edge, or VS Code.*

---

## 📁 Repository Structure
