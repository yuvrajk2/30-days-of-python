# Python Notes – Day 26
## Sorting Algorithms – Bubble, Selection, Insertion, Merge, Quick

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Implement five classic sorting algorithms.
- Analyse the time and space complexity of each.
- Understand when to use each algorithm.
- Use Python's built-in `sort()` and `sorted()`.

---

# Why Learn Sorting Algorithms?

- Core computer science knowledge asked in interviews.
- Understanding trade-offs helps you choose the right algorithm.
- Foundation for more complex algorithms.

---

# Big O Quick Reference

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Python's Timsort | O(n) | O(n log n) | O(n log n) | O(n) |

---

# 1. Bubble Sort

Repeatedly swaps adjacent elements if they are in the wrong order. Largest elements "bubble" to the end.

```python
def bubble_sort(arr: list) -> list:
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:       # already sorted — early exit
            break
    return arr
```

**Example trace:** `[5, 3, 8, 1]`
- Pass 1: `[3, 5, 1, 8]`
- Pass 2: `[3, 1, 5, 8]`
- Pass 3: `[1, 3, 5, 8]` ✓

---

# 2. Selection Sort

Finds the minimum element and places it at the beginning. Repeats for the remaining subarray.

```python
def selection_sort(arr: list) -> list:
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Key trait:** Makes exactly n-1 swaps — best when swaps are expensive.

---

# 3. Insertion Sort

Builds a sorted portion one element at a time by inserting each element into its correct position.

```python
def insertion_sort(arr: list) -> list:
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Best for:** Small arrays or nearly-sorted data (best case O(n)).

---

# 4. Merge Sort

Divide-and-conquer: splits the array in half, sorts each half recursively, then merges them.

```python
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Best for:** Large datasets; stable sort; guaranteed O(n log n).

---

# 5. Quick Sort

Picks a **pivot**, partitions elements into less-than and greater-than groups, then sorts each group recursively.

```python
def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

**In-place version (more efficient):**

```python
def quick_sort_inplace(arr: list, low: int, high: int) -> None:
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

---

# Python's Built-in Sorting

Python uses **Timsort** (a hybrid of merge sort and insertion sort).

```python
nums = [5, 3, 8, 1, 9, 2]

# In-place sort
nums.sort()
nums.sort(reverse=True)

# Returns new sorted list
sorted_nums = sorted(nums)
sorted_desc = sorted(nums, reverse=True)

# Sort with key
students = [("Raj", 85), ("Priya", 92), ("Sam", 78)]
students.sort(key=lambda x: x[1])          # by marks
students.sort(key=lambda x: x[0])          # by name

words = ["banana", "apple", "cherry"]
words.sort(key=len)                          # by length
```

---

# Stability

A sort is **stable** if equal elements maintain their original relative order.

| Algorithm | Stable? |
|-----------|---------|
| Bubble | ✅ |
| Selection | ❌ |
| Insertion | ✅ |
| Merge | ✅ |
| Quick | ❌ (typically) |
| Python Timsort | ✅ |

---

# Practice Questions

## Basic

1. Sort a list using bubble sort and print each pass.
2. Sort a list using selection sort.
3. Sort a list using insertion sort.
4. Sort a list using merge sort.
5. Sort a list using quick sort.
6. Sort strings alphabetically using `sorted()`.
7. Sort a list of tuples by the second element.
8. Sort in descending order.
9. Count the number of comparisons in bubble sort.
10. Check if a list is already sorted.

---

## Intermediate

11. Implement merge sort on a list of strings.
12. Sort a list of dictionaries by a specific key.
13. Find the k-th smallest element using quick select.
14. Count inversions in an array (modified merge sort).
15. Sort a linked list using merge sort.

---

# Mini Project – Sorting Visualizer (Console)

```python
import time
import os

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def visualise(arr, highlight=(), label=""):
    """Print a bar chart of the array."""
    max_val = max(arr) if arr else 1
    width = 40
    print(f"\n  {label}")
    for i, val in enumerate(arr):
        bar_len = int(val / max_val * width)
        bar = "█" * bar_len
        marker = " ◄" if i in highlight else ""
        print(f"  [{i:>2}] {bar:<{width}} {val}{marker}")
    print()

def bubble_sort_viz(arr):
    arr = arr.copy(); n = len(arr); ops = 0
    for i in range(n):
        for j in range(n - i - 1):
            ops += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                visualise(arr, (j, j+1), f"Bubble Sort — pass {i+1}, comparing [{j}] and [{j+1}]")
                time.sleep(0.1)
    return arr, ops

def selection_sort_viz(arr):
    arr = arr.copy(); n = len(arr); ops = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            ops += 1
            if arr[j] < arr[min_idx]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualise(arr, (i, min_idx), f"Selection Sort — placed {arr[i]} at index {i}")
        time.sleep(0.15)
    return arr, ops

def insertion_sort_viz(arr):
    arr = arr.copy(); ops = 0
    for i in range(1, len(arr)):
        key = arr[i]; j = i - 1; ops += 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]; j -= 1; ops += 1
        arr[j+1] = key
        visualise(arr, (j+1,), f"Insertion Sort — inserted {key} at index {j+1}")
        time.sleep(0.15)
    return arr, ops

print("=== Sorting Visualizer ===")
print("1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. All (compare)")
choice = input("Choice: ")

import random
data = random.sample(range(1, 30), 10)
print(f"\nOriginal: {data}")
visualise(data, label="Original Array")

start = time.time()
if choice == "1":
    result, ops = bubble_sort_viz(data)
elif choice == "2":
    result, ops = selection_sort_viz(data)
elif choice == "3":
    result, ops = insertion_sort_viz(data)
else:
    print("\n--- Bubble Sort ---")
    r1, o1 = bubble_sort_viz(data)
    print("\n--- Selection Sort ---")
    r2, o2 = selection_sort_viz(data)
    print("\n--- Insertion Sort ---")
    r3, o3 = insertion_sort_viz(data)
    print(f"\nComparisons — Bubble: {o1}, Selection: {o2}, Insertion: {o3}")
    result, ops = r1, o1

elapsed = time.time() - start
visualise(result, label=f"Sorted! ({ops} comparisons, {elapsed:.3f}s)")
```

---

# Day 26 Summary

After completing Day 26, you should be able to:

- Implement bubble, selection, insertion, merge, and quick sort.
- State the time and space complexity of each.
- Use Python's `sort()` and `sorted()` with custom keys.
- Explain the difference between stable and unstable sorts.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 75 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5 hours**
