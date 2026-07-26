# Python Notes – Day 25
## Binary Search Tree (BST)

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand binary trees and BST properties.
- Implement BST insert, search, and delete.
- Perform in-order, pre-order, and post-order traversals.
- Find min, max, height, and check BST validity.

---

# Binary Tree Basics

A **binary tree** is a tree where each node has at most two children: **left** and **right**.

```
         10
        /   \
       5     15
      / \   /  \
     3   7 12   20
```

---

## Terminology

| Term | Meaning |
|------|---------|
| Root | Top node (no parent) |
| Leaf | Node with no children |
| Height | Longest path from root to leaf |
| Depth | Distance from root to a node |
| Subtree | A node and all its descendants |

---

# Binary Search Tree (BST)

A BST is a binary tree where:
- **Left subtree** contains values **less than** the node.
- **Right subtree** contains values **greater than** the node.
- This holds for every node recursively.

```
         8
        / \
       3   10
      / \    \
     1   6    14
        / \   /
       4   7 13
```

---

## BST Property

For every node:
```
left.value < node.value < right.value
```

---

# BST Implementation

## Node Class

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

---

## BST Class

```python
class BST:
    def __init__(self):
        self.root = None
```

---

## Insert

```python
def insert(self, value):
    self.root = self._insert(self.root, value)

def _insert(self, node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = self._insert(node.left, value)
    elif value > node.value:
        node.right = self._insert(node.right, value)
    # if equal: ignore duplicate
    return node
```

---

## Search

```python
def search(self, value) -> bool:
    return self._search(self.root, value)

def _search(self, node, value) -> bool:
    if node is None:
        return False
    if value == node.value:
        return True
    elif value < node.value:
        return self._search(node.left, value)
    else:
        return self._search(node.right, value)
```

---

## Delete

```python
def delete(self, value):
    self.root = self._delete(self.root, value)

def _delete(self, node, value):
    if node is None:
        return None
    if value < node.value:
        node.left = self._delete(node.left, value)
    elif value > node.value:
        node.right = self._delete(node.right, value)
    else:
        # Case 1: leaf
        if not node.left and not node.right:
            return None
        # Case 2: one child
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        # Case 3: two children — replace with in-order successor
        successor = self._find_min(node.right)
        node.value = successor.value
        node.right = self._delete(node.right, successor.value)
    return node
```

---

## Min and Max

```python
def find_min(self):
    return self._find_min(self.root).value if self.root else None

def _find_min(self, node):
    while node.left:
        node = node.left
    return node

def find_max(self):
    node = self.root
    while node and node.right:
        node = node.right
    return node.value if node else None
```

---

## Height

```python
def height(self) -> int:
    return self._height(self.root)

def _height(self, node) -> int:
    if node is None:
        return 0
    return 1 + max(self._height(node.left), self._height(node.right))
```

---

# Tree Traversals

| Traversal | Order | Use Case |
|-----------|-------|----------|
| In-order | Left → Node → Right | Sorted output |
| Pre-order | Node → Left → Right | Copy a tree |
| Post-order | Left → Right → Node | Delete a tree |
| Level-order | Level by level | BFS |

---

## In-order (Sorted Output)

```python
def inorder(self) -> list:
    result = []
    self._inorder(self.root, result)
    return result

def _inorder(self, node, result):
    if node:
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)
```

---

## Pre-order

```python
def preorder(self) -> list:
    result = []
    self._preorder(self.root, result)
    return result

def _preorder(self, node, result):
    if node:
        result.append(node.value)
        self._preorder(node.left, result)
        self._preorder(node.right, result)
```

---

## Post-order

```python
def postorder(self) -> list:
    result = []
    self._postorder(self.root, result)
    return result

def _postorder(self, node, result):
    if node:
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.value)
```

---

## Level-order (BFS)

```python
from collections import deque

def levelorder(self) -> list[list]:
    if not self.root:
        return []
    result = []
    queue = deque([self.root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

---

## Count Nodes

```python
def count(self) -> int:
    return self._count(self.root)

def _count(self, node) -> int:
    if not node: return 0
    return 1 + self._count(node.left) + self._count(node.right)
```

---

# Validate a BST

```python
def is_valid_bst(self) -> bool:
    return self._is_valid(self.root, float('-inf'), float('inf'))

def _is_valid(self, node, min_val, max_val) -> bool:
    if not node: return True
    if node.value <= min_val or node.value >= max_val:
        return False
    return (self._is_valid(node.left, min_val, node.value) and
            self._is_valid(node.right, node.value, max_val))
```

---

# BST Time Complexity

| Operation | Average | Worst (unbalanced) |
|-----------|---------|-------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

---

# Practice Questions

## Basic

1. Insert values into a BST and verify the structure.
2. Search for a value and print whether it exists.
3. Find the minimum and maximum values.
4. Print all values in sorted order (in-order traversal).
5. Find the height of the tree.
6. Count the total number of nodes.
7. Delete a leaf node.
8. Delete a node with one child.
9. Delete a node with two children.
10. Print the level-order traversal.

---

## Intermediate

11. Check if a binary tree is a valid BST.
12. Find the lowest common ancestor (LCA) of two nodes.
13. Check if the BST is balanced.
14. Find the k-th smallest element.
15. Build a BST from a sorted list (balanced).

---

# Mini Project – BST Implementation

```python
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self): self.root = None

    # --- Insert ---
    def insert(self, v): self.root = self._ins(self.root, v)
    def _ins(self, n, v):
        if not n: return Node(v)
        if v < n.value: n.left = self._ins(n.left, v)
        elif v > n.value: n.right = self._ins(n.right, v)
        return n

    # --- Search ---
    def search(self, v) -> bool: return self._srch(self.root, v)
    def _srch(self, n, v):
        if not n: return False
        if v == n.value: return True
        return self._srch(n.left, v) if v < n.value else self._srch(n.right, v)

    # --- Delete ---
    def delete(self, v): self.root = self._del(self.root, v)
    def _del(self, n, v):
        if not n: return None
        if v < n.value: n.left = self._del(n.left, v)
        elif v > n.value: n.right = self._del(n.right, v)
        else:
            if not n.left: return n.right
            if not n.right: return n.left
            s = n.right
            while s.left: s = s.left
            n.value = s.value
            n.right = self._del(n.right, s.value)
        return n

    # --- Properties ---
    def find_min(self):
        n = self.root
        while n and n.left: n = n.left
        return n.value if n else None

    def find_max(self):
        n = self.root
        while n and n.right: n = n.right
        return n.value if n else None

    def height(self): return self._ht(self.root)
    def _ht(self, n): return 0 if not n else 1 + max(self._ht(n.left), self._ht(n.right))

    def count(self): return self._cnt(self.root)
    def _cnt(self, n): return 0 if not n else 1 + self._cnt(n.left) + self._cnt(n.right)

    # --- Traversals ---
    def inorder(self):
        r = []; self._io(self.root, r); return r
    def _io(self, n, r):
        if n: self._io(n.left, r); r.append(n.value); self._io(n.right, r)

    def preorder(self):
        r = []; self._po(self.root, r); return r
    def _po(self, n, r):
        if n: r.append(n.value); self._po(n.left, r); self._po(n.right, r)

    def levelorder(self):
        if not self.root: return []
        res, q = [], deque([self.root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.value)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res

    def is_valid(self): return self._val(self.root, float('-inf'), float('inf'))
    def _val(self, n, lo, hi):
        if not n: return True
        if not lo < n.value < hi: return False
        return self._val(n.left, lo, n.value) and self._val(n.right, n.value, hi)

# --- Demo ---
bst = BST()
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for v in values:
    bst.insert(v)

print("Values inserted:", values)
print("In-order (sorted):", bst.inorder())
print("Pre-order:        ", bst.preorder())
print("Level-order:      ", bst.levelorder())
print(f"Min: {bst.find_min()}, Max: {bst.find_max()}")
print(f"Height: {bst.height()}, Nodes: {bst.count()}")
print(f"Search 6: {bst.search(6)}, Search 99: {bst.search(99)}")
print(f"Valid BST: {bst.is_valid()}")

bst.delete(3)
print("\nAfter deleting 3:")
print("In-order:", bst.inorder())

MENU = "\n1.Insert 2.Search 3.Delete 4.Inorder 5.Min/Max 6.Height 0.Exit\n"
while True:
    print(MENU, end="")
    c = input("Choice: ")
    if c == "1":
        v = int(input("Value: ")); bst.insert(v); print(f"Inserted {v}. Tree:", bst.inorder())
    elif c == "2":
        v = int(input("Value: ")); print(f"{v} found: {bst.search(v)}")
    elif c == "3":
        v = int(input("Value: ")); bst.delete(v); print(f"Deleted {v}. Tree:", bst.inorder())
    elif c == "4":
        print("In-order:", bst.inorder())
    elif c == "5":
        print(f"Min: {bst.find_min()}, Max: {bst.find_max()}")
    elif c == "6":
        print(f"Height: {bst.height()}")
    elif c == "0":
        break
```

---

# Day 25 Summary

After completing Day 25, you should be able to:

- Implement a BST with insert, search, and delete.
- Perform in-order, pre-order, post-order, and level-order traversals.
- Find min, max, height, and node count.
- Validate whether a binary tree satisfies the BST property.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 75 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5–4 hours**
