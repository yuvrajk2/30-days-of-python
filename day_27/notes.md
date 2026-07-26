# Python Notes – Day 27
## Searching Algorithms – Linear Search, Binary Search, and Algorithm Analysis

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Search an unsorted collection with linear search.
- Search a sorted collection efficiently with binary search.
- Explain why binary search requires sorted data.
- Compare algorithms using time and space complexity.
- Choose an appropriate search strategy for a problem.

---

# What Is Searching?

Searching means locating a target value in a collection. A search function
usually returns the position of the value, or a clear result such as `-1`
when the value is not present.

```python
numbers = [12, 4, 19, 7]
target = 19
```

The target `19` is at index `2`. Remember that Python sequences use
zero-based indexing.

---

# 1. Linear Search

Linear search checks values one at a time from left to right. It works on
both sorted and unsorted data.

```python
def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

numbers = [12, 4, 19, 7]
print(linear_search(numbers, 19))  # 2
print(linear_search(numbers, 10))  # -1
```

## Complexity

- Best case: **O(1)** when the first item matches.
- Average case: **O(n)**.
- Worst case: **O(n)** when the item is last or absent.
- Extra space: **O(1)**.

Linear search is a good default for small or unsorted collections.

---

# 2. Binary Search

Binary search repeatedly checks the middle item and discards half of the
remaining search range. The input **must already be sorted**.

```python
def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        middle = (low + high) // 2

        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1

numbers = [4, 7, 12, 19, 23, 31]
print(binary_search(numbers, 19))  # 3
print(binary_search(numbers, 10))  # -1
```

## Complexity

- Best case: **O(1)**.
- Average and worst case: **O(log n)**.
- Extra space for the iterative version: **O(1)**.

For example, a collection of 1,000,000 items needs at most about 20
halving steps in binary search, provided the data is sorted.

---

# Recursive Binary Search

Binary search can also be written recursively. Each call receives a smaller
range of indexes.

```python
def recursive_binary_search(items, target, low, high):
    if low > high:
        return -1

    middle = (low + high) // 2
    if items[middle] == target:
        return middle
    if items[middle] < target:
        return recursive_binary_search(items, target, middle + 1, high)
    return recursive_binary_search(items, target, low, middle - 1)

numbers = [4, 7, 12, 19, 23, 31]
index = recursive_binary_search(numbers, 23, 0, len(numbers) - 1)
print(index)  # 4
```

The recursive version has **O(log n)** time and **O(log n)** call-stack
space. The iterative version is usually preferable when both are clear.

---

# First and Last Occurrence

If a sorted list contains duplicates, ordinary binary search may find any
matching index. To find the first occurrence, keep searching left after a
match:

```python
def first_occurrence(items, target):
    low, high = 0, len(items) - 1
    answer = -1

    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            answer = middle
            high = middle - 1
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return answer

print(first_occurrence([1, 2, 2, 2, 5], 2))  # 1
```

---

# Algorithm Analysis

When comparing algorithms, consider:

1. **Correctness** – does it return the right answer for all valid inputs?
2. **Time complexity** – how does the number of operations grow?
3. **Space complexity** – how much extra memory is required?
4. **Input requirements** – for example, binary search needs sorted data.
5. **Practical cost** – constants, readability, and the cost of preparing data.

Sorting a list once may make many future binary searches worthwhile. For one
search on an unsorted list, sorting first can cost more than linear search.

| Algorithm | Required input | Best | Average | Worst | Extra space |
|-----------|----------------|------|---------|-------|-------------|
| Linear search | Any sequence | O(1) | O(n) | O(n) | O(1) |
| Binary search | Sorted sequence | O(1) | O(log n) | O(log n) | O(1) iterative |

---

# Python's Search Tools

For membership, use `in` when you do not need an index:

```python
names = ["Asha", "Ben", "Chen"]
print("Ben" in names)  # True
```

For a sorted list, the standard library provides binary-search helpers:

```python
from bisect import bisect_left

numbers = [10, 20, 30, 40]
position = bisect_left(numbers, 30)
found = position < len(numbers) and numbers[position] == 30
print(found)  # True
```

---

# Practice Questions

## Basic

1. Implement linear search for a list of strings.
2. Return all indexes where a target occurs.
3. Count comparisons made by a linear search.
4. Implement iterative binary search.
5. Explain why binary search fails on an unsorted list.

## Intermediate

6. Implement recursive binary search.
7. Find the first and last occurrence of a duplicate value.
8. Find the insertion position of a target in a sorted list.
9. Search a rotated sorted list.
10. Compare linear and binary search on lists of different sizes.

---

# Mini Project – Search Utility

Build a menu-driven utility that:

1. Accepts a list of integers from the user.
2. Offers linear search and binary search.
3. Sorts a copy before binary search without changing the original list.
4. Displays the found index and the number of comparisons.
5. Handles missing values and invalid input.

```python
def linear_search_count(items, target):
    comparisons = 0
    for index, item in enumerate(items):
        comparisons += 1
        if item == target:
            return index, comparisons
    return -1, comparisons

def binary_search_count(items, target):
    low, high = 0, len(items) - 1
    comparisons = 0

    while low <= high:
        middle = (low + high) // 2
        comparisons += 1
        if items[middle] == target:
            return middle, comparisons
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1, comparisons

values = [18, 4, 27, 9, 13, 31, 6]
target = 13

linear_result = linear_search_count(values, target)
sorted_values = sorted(values)
binary_result = binary_search_count(sorted_values, target)

print(f"Original list: {values}")
print(f"Linear search: index={linear_result[0]}, comparisons={linear_result[1]}")
print(f"Sorted list: {sorted_values}")
print(f"Binary search: index={binary_result[0]}, comparisons={binary_result[1]}")
```

---

# Day 27 Summary

After completing Day 27, you should be able to:

- Implement linear and binary search.
- Explain the sorted-input requirement for binary search.
- Compare algorithms using Big O notation.
- Use `bisect` for searches in sorted sequences.
- Build a search utility that reports useful performance information.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3–3.5 hours**