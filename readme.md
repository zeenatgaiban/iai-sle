# SLE-2: Empirical Performance Analysis of BFS and DFS

## Student Details

**Name:** Anusha Anil Raybagi  
**PRN:** 25UAM119  
**Course:** Introduction to Artificial Intelligence  
**Course Code:** 02AML204  
**Program:** SY B.Tech. CSE (AI & ML)

---

## Experiment

**SLE-2 – Profiling Report (Empirical Performance Analysis)**

## Topic

**Performance Comparison of Breadth First Search (BFS) and Depth First Search (DFS)**

---

## 1. Objective

The objective of this experiment is to compare the empirical performance of BFS and DFS using:

- Execution time
- Number of nodes expanded
- Different search cases
- Py-Spy profiling

The same graph and search problem are used for both algorithms.

---

## 2. Algorithms Used

### Breadth First Search (BFS)

BFS explores the graph level by level using a queue.

### Depth First Search (DFS)

DFS explores one branch deeply before backtracking using a stack.

---

## 3. Graph Used

The experiment uses a small graph containing nodes from **A to T**.

The starting node is:

**A**

The graph used is:

```text
                    A
                 /  |  \
                B   C   D
              / \   |   / \
             E   F  G  H   I
             |  / \ / \  / \
             J K  L M N O  P Q
             | |  |
             R S  T
```
