# Python Notes – Day 23
## Hash Tables, Dictionaries, and Sets (Deep Dive)

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand how hash tables work internally.
- Use dictionaries as hash tables for O(1) lookups.
- Use `collections.defaultdict`, `Counter`, and `OrderedDict`.
- Solve classic hash table problems.

---

# What is a Hash Table?

A hash table maps **keys** to **values** using a **hash function** that converts a key into an index.

```
key  → hash(key)  → index → value
"Raj" → 1234567   → 3     → 85
```

---

## Why Hash Tables?

| Operation | Array/List | Hash Table (dict) |
|-----------|-----------|-------------------|
| Access    | O(1) by index | O(1) by key |
| Search    | O(n) | O(1) avg |
| Insert    | O(n) | O(1) avg |
| Delete    | O(n) | O(1) avg |

---

## How Python Dicts Work

Python's `dict` is a hash table:
- Keys are hashed with `hash()`.
- Collisions are handled by open addressing.
- Load factor is kept low; table is resized when needed.

```python
print(hash("hello"))    # consistent within a session
print(hash(42))         # 42
print(hash(3.14))       # some large int
```

Only **hashable** (immutable) types can be keys: `str`, `int`, `float`, `bool`, `tuple`.

---

## Building a Simple Hash Table

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value; return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = [p for p in self.table[index] if p[0] != key]

    def __str__(self):
        return str({p[0]: p[1] for bucket in self.table for p in bucket})

ht = HashTable()
ht.set("name", "Raj")
ht.set("age", 20)
print(ht)
print(ht.get("name"))
ht.delete("age")
print(ht)
```

---

# `collections.defaultdict`

A dict that provides a default value when a key is missing.

```python
from collections import defaultdict

# Default: list
word_positions = defaultdict(list)
words = "the cat sat on the mat".split()
for i, word in enumerate(words):
    word_positions[word].append(i)

print(dict(word_positions))
# {'the': [0, 4], 'cat': [1], 'sat': [2], 'on': [3], 'mat': [5]}

# Default: int (0)
char_count = defaultdict(int)
for ch in "mississippi":
    char_count[ch] += 1

print(dict(char_count))
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

---

# `collections.Counter`

Counts hashable objects.

```python
from collections import Counter

text = "the quick brown fox jumps over the lazy dog"
word_count = Counter(text.split())

print(word_count.most_common(3))   # [('the', 2), ...]

# Arithmetic
c1 = Counter("aab")
c2 = Counter("bcc")
print(c1 + c2)    # Counter({'a': 2, 'c': 2, 'b': 2})
print(c1 - c2)    # Counter({'a': 2})
print(c1 & c2)    # intersection: min counts
print(c1 | c2)    # union: max counts
```

---

# `collections.OrderedDict`

Preserves insertion order (all Python 3.7+ dicts do too, but `OrderedDict` has extra methods).

```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3

od.move_to_end("a")         # move to end
od.move_to_end("c", last=False)  # move to beginning
print(list(od.keys()))      # ['c', 'b', 'a']
```

---

# Sets as Hash Sets

Sets are hash tables with only keys (no values). O(1) average for add, remove, and lookup.

```python
seen = set()
nums = [1, 2, 3, 2, 1, 4]
unique = []
for n in nums:
    if n not in seen:
        seen.add(n)
        unique.append(n)
print(unique)   # [1, 2, 3, 4]
```

---

# Classic Hash Table Problems

## Two Sum

```python
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return (-1, -1)

print(two_sum([2, 7, 11, 15], 9))   # (0, 1)
```

---

## First Non-Repeating Character

```python
from collections import Counter

def first_unique(s: str) -> str:
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return ""

print(first_unique("leetcode"))   # 'l'
print(first_unique("aabb"))       # ''
```

---

## Group Anagrams

```python
from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
```

---

## Check if Two Strings are Anagrams

```python
from collections import Counter

def are_anagrams(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)
```

---

# LRU Cache (Bonus)

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
print(cache.get(1))   # 10
cache.put(3, 30)      # evicts key 2
print(cache.get(2))   # -1
```

---

# Practice Questions

## Basic

1. Count the frequency of each character in a string.
2. Find the most common word in a sentence.
3. Check if two strings are anagrams.
4. Remove duplicates from a list while preserving order.
5. Find all elements that appear more than once.
6. Group words by their first letter.
7. Create a frequency map from a list of integers.
8. Find the first repeated element in a list.
9. Check if a string has all unique characters.
10. Find the intersection and union of two lists using sets.

---

## Intermediate

11. Solve the Two Sum problem.
12. Find the first non-repeating character.
13. Group anagrams together.
14. Implement an LRU cache.
15. Find the longest substring without repeating characters.

---

# Mini Project – Word Frequency Counter

```python
import re
from collections import Counter, defaultdict
from pathlib import Path

def analyse_text(text: str) -> None:
    # Clean and tokenise
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    total_words = len(words)

    if total_words == 0:
        print("No words found.")
        return

    counter = Counter(words)
    unique_words = len(counter)
    avg_length = sum(len(w) for w in words) / total_words

    # Group words by length
    by_length = defaultdict(list)
    for word in counter:
        by_length[len(word)].append(word)

    # Display
    print(f"\n{'=' * 40}")
    print(f"  WORD FREQUENCY ANALYSIS")
    print(f"{'=' * 40}")
    print(f"Total words:   {total_words}")
    print(f"Unique words:  {unique_words}")
    print(f"Avg word len:  {avg_length:.2f}")

    print(f"\nTop 10 most common words:")
    for word, count in counter.most_common(10):
        bar = "█" * count
        print(f"  {word:<15} {count:>4}  {bar}")

    print(f"\nWords by length:")
    for length in sorted(by_length)[:6]:
        print(f"  {length} letters: {', '.join(sorted(by_length[length])[:5])}")

    print(f"\nWords appearing only once: {sum(1 for c in counter.values() if c == 1)}")

print("=== Word Frequency Counter ===")
print("1. Analyse sample text")
print("2. Enter your own text")
choice = input("Choice: ")

if choice == "1":
    sample = """
    Python is a versatile programming language. Python is easy to learn and Python
    is widely used in web development, data science, machine learning, and automation.
    Many programmers choose Python because Python has clear and readable syntax.
    Python supports multiple programming paradigms including object-oriented programming.
    """
    analyse_text(sample)
elif choice == "2":
    print("Enter text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "": break
        lines.append(line)
    analyse_text(" ".join(lines))
```

---

# Day 23 Summary

After completing Day 23, you should be able to:

- Explain how hash tables work internally.
- Use `defaultdict`, `Counter`, and `OrderedDict`.
- Solve classic problems: Two Sum, anagrams, LRU cache.
- Leverage sets for O(1) membership checks.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
