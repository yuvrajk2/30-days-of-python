# Python Notes – Day 21
## Arrays, Linked Lists – Concepts and Python Implementation

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand arrays and their properties.
- Use Python's `array` module.
- Understand linked list concepts (singly and doubly linked).
- Implement a linked list in Python from scratch.
- Compare arrays vs linked lists.

---

# Arrays

An array is a **fixed-size, contiguous block of memory** storing elements of the **same type**.

## Python's Built-in `list` vs Array

| Feature | `list` | `array` |
|---------|--------|---------|
| Types | Mixed | Single type |
| Memory | More overhead | Less overhead |
| Speed | Slower (type checks) | Faster for numeric ops |
| Use case | General | Numeric/binary data |

---

## Python `array` Module

```python
from array import array

# Type codes: 'i'=int, 'f'=float, 'd'=double, 'b'=byte
nums = array('i', [1, 2, 3, 4, 5])

print(nums[0])     # 1
nums.append(6)
nums.remove(3)
print(len(nums))   # 5
print(list(nums))  # [1, 2, 4, 5, 6]
```

---

## Array Type Codes

| Code | Type | Size |
|------|------|------|
| `'b'` | signed byte | 1 byte |
| `'B'` | unsigned byte | 1 byte |
| `'h'` | signed short | 2 bytes |
| `'i'` | signed int | 2 bytes |
| `'l'` | signed long | 4 bytes |
| `'f'` | float | 4 bytes |
| `'d'` | double | 8 bytes |

---

## Common Array Operations

| Operation | Time Complexity |
|-----------|----------------|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Insertion at end | O(1) amortised |
| Insertion at beginning | O(n) |
| Deletion | O(n) |

---

# NumPy Arrays (Bonus)

For serious numeric work:

```python
import numpy as np   # pip install numpy

a = np.array([1, 2, 3, 4, 5])
print(a * 2)        # [2, 4, 6, 8, 10]
print(a.mean())     # 3.0
print(a.sum())      # 15
print(a[1:4])       # [2, 3, 4]
```

---

# Linked Lists

A **linked list** is a linear data structure where each element (**node**) stores a value and a **pointer (reference)** to the next node.

```
[data|next] → [data|next] → [data|next] → None
  Head                         Tail
```

---

## Why Linked Lists?

| Operation | Array/List | Linked List |
|-----------|-----------|-------------|
| Access by index | O(1) ✅ | O(n) |
| Insert at beginning | O(n) | O(1) ✅ |
| Insert at end | O(1) | O(1) with tail |
| Delete at beginning | O(n) | O(1) ✅ |
| Memory | Contiguous | Non-contiguous |

Use linked lists when you frequently insert/delete at the beginning.

---

## Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer to next node
```

---

## Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add to the end."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add to the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Remove first node with given data."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data) -> bool:
        """Return True if data exists."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        """Reverse the list in place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self) -> str:
        return " → ".join(str(x) for x in self.to_list()) + " → None"
```

---

## Usage

```python
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)

print(ll)          # 0 → 1 → 2 → 3 → None
print(ll.length()) # 4
print(ll.search(2))  # True

ll.delete(2)
print(ll)          # 0 → 1 → 3 → None

ll.reverse()
print(ll)          # 3 → 1 → 0 → None
```

---

## Doubly Linked List

Each node has both `next` and `prev` pointers.

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def __str__(self) -> str:
        parts = []
        current = self.head
        while current:
            parts.append(str(current.data))
            current = current.next
        return " ⇌ ".join(parts)
```

---

# Common Interview Problems

1. Detect a cycle in a linked list (Floyd's algorithm).
2. Find the middle node.
3. Reverse a linked list.
4. Merge two sorted linked lists.
5. Remove nth node from the end.

---

# Practice Questions

## Basic

1. Implement a linked list and append 5 elements.
2. Print all elements of a linked list.
3. Find the length of a linked list.
4. Search for an element in a linked list.
5. Delete a node from a linked list.
6. Reverse a linked list.
7. Convert a linked list to a Python list.
8. Insert a node at a given position.
9. Find the middle element.
10. Count occurrences of a value.

---

## Intermediate

11. Detect a cycle using Floyd's algorithm.
12. Merge two sorted linked lists.
13. Remove duplicates from a linked list.
14. Implement a doubly linked list with `append`, `prepend`, and `delete`.
15. Rotate a linked list by k positions.

---

# Mini Project – Custom Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node; return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = node

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at(self, index, data):
        if index == 0: self.prepend(data); return
        node = Node(data)
        cur = self.head
        for _ in range(index - 1):
            if not cur: raise IndexError("Index out of range")
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def delete(self, data):
        if not self.head: return
        if self.head.data == data: self.head = self.head.next; return
        cur = self.head
        while cur.next:
            if cur.next.data == data: cur.next = cur.next.next; return
            cur = cur.next

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
        self.head = prev

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self) -> bool:
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
            if slow is fast: return True
        return False

    def to_list(self): 
        result, cur = [], self.head
        while cur: result.append(cur.data); cur = cur.next
        return result

    def __str__(self): 
        return " → ".join(map(str, self.to_list())) + " → None"
    def __len__(self): 
        return len(self.to_list())

# Demo
ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.append(val)

print("List:      ", ll)
ll.prepend(5)
print("Prepend 5: ", ll)
ll.insert_at(3, 25)
print("Insert 25: ", ll)
ll.delete(25)
print("Delete 25: ", ll)
print("Middle:    ", ll.find_middle())
ll.reverse()
print("Reversed:  ", ll)
print("Length:    ", len(ll))
print("Has cycle: ", ll.has_cycle())
```

---

# Day 21 Summary

After completing Day 21, you should be able to:

- Use Python's `array` module for typed arrays.
- Implement a singly and doubly linked list from scratch.
- Perform append, prepend, insert, delete, reverse, and search.
- Understand the time complexity of each operation.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5 hours**
