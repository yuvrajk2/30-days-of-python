# Python Notes – Day 22
## Stack, Queue, and Heap

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand and implement Stack (LIFO) and Queue (FIFO).
- Use Python's `collections.deque` for efficient queue operations.
- Use `queue.Queue` and `queue.LifoQueue`.
- Understand heaps and use Python's `heapq` module.
- Implement a priority queue.

---

# Stack

A stack follows **LIFO** — Last In, First Out.

```
Push → [5][4][3][2][1] ← Top
Pop  ←
```

### Real-world examples

- Undo/Redo in editors.
- Browser back-button history.
- Function call stack.
- Balanced parentheses checker.

---

## Stack Using Python List

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek on empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"Stack(top → {self._data[::-1]})"

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)          # Stack(top → [30, 20, 10])
print(s.peek())   # 30
print(s.pop())    # 30
print(s.size())   # 2
```

---

## Stack Time Complexity

| Operation | Time |
|-----------|------|
| push | O(1) |
| pop | O(1) |
| peek | O(1) |
| search | O(n) |

---

## Application – Balanced Parentheses

```python
def is_balanced(expr: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("({[]})"))   # True
print(is_balanced("({[})"))    # False
```

---

## Application – Reverse a String

```python
def reverse_string(s: str) -> str:
    stack = list(s)
    return "".join(stack.pop() for _ in range(len(stack)))
```

---

# Queue

A queue follows **FIFO** — First In, First Out.

```
Enqueue → [1][2][3][4][5] → Dequeue
            Rear         Front
```

### Real-world examples

- Print queue.
- CPU task scheduling.
- BFS (Breadth-First Search).

---

## Queue Using `collections.deque`

`deque` (double-ended queue) is O(1) for both ends — prefer it over a plain list.

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)       # add to right (rear)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.popleft()   # remove from left (front)

    def front(self):
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return f"Queue(front → {list(self._data)})"

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q)            # Queue(front → ['A', 'B', 'C'])
print(q.dequeue())  # A
print(q.size())     # 2
```

---

## `queue` Module (Thread-Safe)

```python
import queue

# FIFO queue
q = queue.Queue()
q.put(1)
q.put(2)
print(q.get())   # 1

# LIFO queue (Stack)
lifo = queue.LifoQueue()
lifo.put(1)
lifo.put(2)
print(lifo.get())  # 2

# Priority queue
pq = queue.PriorityQueue()
pq.put((2, "medium"))
pq.put((1, "high"))
pq.put((3, "low"))
print(pq.get())   # (1, 'high')
```

---

## Deque as Deque (Double-Ended Queue)

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)    # [0, 1, 2, 3]
d.append(4)        # [0, 1, 2, 3, 4]
d.popleft()        # 0
d.pop()            # 4
d.rotate(1)        # [3, 1, 2]
```

---

# Heap

A **heap** is a complete binary tree where:
- **Min-heap**: parent ≤ children (smallest at top).
- **Max-heap**: parent ≥ children (largest at top).

Python's `heapq` implements a **min-heap**.

---

## `heapq` Module

```python
import heapq

nums = [5, 1, 8, 3, 9, 2]
heapq.heapify(nums)    # converts list to heap in-place
print(nums)            # [1, 3, 2, 5, 9, 8] (heap order)

heapq.heappush(nums, 0)
print(heapq.heappop(nums))   # 0 (smallest)
print(heapq.heappop(nums))   # 1
```

---

## `heapq` Functions

| Function | Description |
|----------|-------------|
| `heapify(lst)` | Convert list to heap |
| `heappush(heap, item)` | Push item |
| `heappop(heap)` | Pop smallest item |
| `heappushpop(heap, item)` | Push then pop |
| `heapreplace(heap, item)` | Pop then push |
| `nlargest(n, lst)` | n largest items |
| `nsmallest(n, lst)` | n smallest items |

```python
import heapq

data = [3, 1, 4, 1, 5, 9, 2, 6]
print(heapq.nlargest(3, data))    # [9, 6, 5]
print(heapq.nsmallest(3, data))   # [1, 1, 2]
```

---

## Max-Heap (Negate Values)

Python's `heapq` is min-heap only. Simulate max-heap by negating:

```python
import heapq

max_heap = []
for val in [3, 1, 4, 1, 5]:
    heapq.heappush(max_heap, -val)

while max_heap:
    print(-heapq.heappop(max_heap), end=" ")   # 5 4 3 1 1
```

---

## Priority Queue Using heapq

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0    # tie-breaker

    def push(self, priority, item):
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self):
        return heapq.heappop(self._heap)[2]   # return just the item

    def peek(self):
        return self._heap[0][2]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

pq = PriorityQueue()
pq.push(3, "low priority task")
pq.push(1, "urgent task")
pq.push(2, "normal task")

while not pq.is_empty():
    print(pq.pop())
```

---

# Heap Time Complexity

| Operation | Time |
|-----------|------|
| heapify | O(n) |
| heappush | O(log n) |
| heappop | O(log n) |
| peek | O(1) |

---

# Practice Questions

## Basic

1. Implement a stack and demonstrate push, pop, and peek.
2. Use a stack to reverse a string.
3. Check for balanced parentheses using a stack.
4. Implement a queue using `deque`.
5. Implement `enqueue`, `dequeue`, and `front`.
6. Use `heapq.heapify` to find the smallest 3 elements.
7. Use `heapq.nlargest` to find top 5 scores.
8. Implement a max-heap using negation.
9. Implement a priority queue.
10. Use `queue.LifoQueue` as a stack.

---

## Intermediate

11. Evaluate a postfix expression using a stack.
12. Convert infix to postfix notation using a stack.
13. Implement a queue using two stacks.
14. Simulate a print queue (tasks with priorities).
15. Find the k-th largest element using a heap.

---

# Mini Project – Stack Calculator (Postfix/RPN Evaluator)

```python
class StackCalculator:
    """
    Evaluates Reverse Polish Notation (postfix) expressions.
    Example: "3 4 + 2 *" = (3+4)*2 = 14
    """

    def __init__(self):
        self._stack = []
        self.OPERATORS = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '**': lambda a, b: a ** b,
            '%': lambda a, b: a % b,
        }

    def evaluate(self, expression: str) -> float:
        self._stack = []
        tokens = expression.strip().split()

        for token in tokens:
            if token in self.OPERATORS:
                if len(self._stack) < 2:
                    raise ValueError(f"Not enough operands for '{token}'")
                b = self._stack.pop()
                a = self._stack.pop()
                result = self.OPERATORS[token](a, b)
                self._stack.append(result)
            else:
                try:
                    self._stack.append(float(token))
                except ValueError:
                    raise ValueError(f"Unknown token: '{token}'")

        if len(self._stack) != 1:
            raise ValueError("Invalid expression")
        return self._stack[0]


calc = StackCalculator()

tests = [
    ("3 4 +",         7),
    ("5 1 2 + 4 * + 3 -",  14),
    ("2 3 ** 1 -",    7),
    ("15 7 1 1 + - / 3 * 2 1 1 + + -", 5),
]

print("=== Stack (RPN) Calculator ===\n")
for expr, expected in tests:
    result = calc.evaluate(expr)
    status = "✓" if abs(result - expected) < 1e-9 else "✗"
    print(f"  {status}  {expr:40s} = {result}")

print("\nInteractive mode (enter RPN expression, 'quit' to exit):")
while True:
    expr = input("RPN > ").strip()
    if expr.lower() in ("quit", "exit"): break
    try:
        print(f"  = {calc.evaluate(expr)}")
    except Exception as e:
        print(f"  Error: {e}")
```

---

# Day 22 Summary

After completing Day 22, you should be able to:

- Implement a stack with push, pop, peek.
- Implement a queue with enqueue and dequeue using `deque`.
- Use Python's `heapq` module for min-heap operations.
- Build a priority queue with `heapq`.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5 hours**
