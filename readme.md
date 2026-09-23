
# SLE-2: Empirical Performance Analysis of BFS and DFS

## Student Details

**Name:** Jeenat Faiyaz Gaiban 
**PRN:** 25UAM121  
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

The experiment uses a graph containing nodes from **A to Z**.

The starting node is:

**A**

The graph used is:

```text
                         A
                    /    |    \
                   B     C     D
                 /  \    |    / \
                E    F   G    H   I
                |   / \ / \  / \
                J  K  L M N O  P Q
                |  |  | | | |  | |
                R  S  T U V W  X Y
                |
                Z
```

### Graph Representation Used in the Program

```python
graph = {
    'A': ['B', 'C', 'D'],

    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],

    'E': ['J'],
    'F': ['K', 'L'],
    'G': ['M', 'N'],
    'H': ['O'],
    'I': ['P', 'Q'],

    'J': ['R'],
    'K': ['S'],
    'L': ['T'],
    'M': ['U'],
    'N': ['V'],

    'O': ['W'],
    'P': ['X'],
    'Q': ['Y'],
    'R': ['Z'],

    'S': [],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': []
}
```

---

## 4. Cases Tested

| Case | Start | Goal |
|------|-------|------|
| Best Case | A | B |
| Average Case | A | M |
| Worst Case | A | Z |

Each algorithm was executed **3 times** for every case.

---

## 5. Performance Metrics

The following metrics were measured:

1. Average execution time in milliseconds
2. Number of nodes expanded

Python's `time.perf_counter()` was used to measure execution time.

Py-Spy was also used as an additional profiling tool.

---

## 6. Experimental Results

The values below should be filled using the actual output obtained from `benchmark.py`.

| Case | Algorithm | Nodes Expanded | Average Time (ms) |
|------|-----------|----------------|-------------------|
| Best | BFS | **ENTER ACTUAL VALUE** | **ENTER ACTUAL VALUE** |
| Best | DFS | **ENTER ACTUAL VALUE** | **ENTER ACTUAL VALUE** |
| Average | BFS | **ENTER ACTUAL VALUE** | **ENTER ACTUAL VALUE** |
| Average | DFS | **ENTER ACTUAL VALUE** | **ENTER ACTUAL VALUE** |
| Worst | BFS | **ENTER ACTUAL VALUE** | **ENTER ACTUAL VALUE** |
| Worst | DFS | **ENTER ACTUAL VALUE** | **ENTER ACTUAL VALUE** |

> **Note:** The experimental values should be taken directly from the actual program output and should not be manually estimated.

---

## 7. Search Paths

### Best Case

**Goal:** B

BFS:

```text
A → B
```

DFS:

```text
A → B
```

### Average Case

**Goal:** M

The exact BFS and DFS paths should be taken from the actual program output.

BFS:

```text
PASTE ACTUAL BFS PATH
```

DFS:

```text
PASTE ACTUAL DFS PATH
```

### Worst Case

**Goal:** Z

The exact BFS and DFS paths should be taken from the actual program output.

BFS:

```text
PASTE ACTUAL BFS PATH
```

DFS:

```text
PASTE ACTUAL DFS PATH
```

---

## 8. Profiling Using Py-Spy

Py-Spy was used as an additional profiling tool to observe the runtime behavior of the Python search program.

A profiling file named:

```text
profile.svg
```

was generated using Py-Spy.

The profiling program repeatedly executes BFS and DFS so that Py-Spy can collect sufficient samples.

The Py-Spy profiling result is included in the project as:

```text
profile.svg
```

---

## 9. Observation

The experiment was performed using the same A–Z graph for BFS and DFS.

The number of nodes expanded and average execution time were recorded for the best, average, and worst cases.

The execution time and node expansion can differ depending on the search case and the order in which nodes are explored.

Since the graph used in the experiment is small, the measured execution times may be very small. Therefore, the number of nodes expanded provides an additional metric for observing the search effort of both algorithms.

The observations are based on the actual execution of the implemented programs.

---

## 10. Tools Used

- Python
- `time.perf_counter()`
- Py-Spy
- VS Code
- PowerShell
- GitHub

---

## 11. Files in This Project

```text
SLE2_IAI/
│
├── bfs_dfs.py
├── benchmark.py
├── profile_search.py
├── profile.svg
├── README.md
└── contribution.md
```

### File Description

- **bfs_dfs.py** – Contains the A–Z graph and BFS/DFS algorithms.
- **benchmark.py** – Measures execution time and nodes expanded for the three cases.
- **profile_search.py** – Runs BFS and DFS repeatedly for Py-Spy profiling.
- **profile.svg** – Py-Spy profiling output.
- **README.md** – Project information and experimental details.
- **contribution.md** – Student and AI contribution details.

---

## 12. Conclusion

BFS and DFS were implemented and tested on the same A–Z graph under best, average, and worst search cases.

Execution time and nodes expanded were recorded for comparison.

Py-Spy was additionally used to profile the search program.

The experiment demonstrates how empirical measurements can be used along with theoretical understanding to analyze the performance of search algorithms.
```

