from collections import deque

# Graph from A to Z
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


# ---------------- BFS ----------------

def bfs(graph, start, goal):

    queue = deque([(start, [start])])
    visited = set()
    nodes = 0

    while queue:

        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes += 1

        if current == goal:
            return path, nodes

        for neighbour in graph[current]:

            if neighbour not in visited:
                queue.append(
                    (neighbour, path + [neighbour])
                )

    return None, nodes


# ---------------- DFS ----------------

def dfs(graph, start, goal):

    stack = [(start, [start])]
    visited = set()
    nodes = 0

    while stack:

        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes += 1

        if current == goal:
            return path, nodes

        # Reverse maintains left-to-right traversal
        for neighbour in reversed(graph[current]):

            if neighbour not in visited:
                stack.append(
                    (neighbour, path + [neighbour])
                )

    return None, nodes


# ---------------- Test Cases ----------------

cases = [
    ("Best Case", "B"),
    ("Average Case", "M"),
    ("Worst Case", "Z")
]


# ---------------- Run BFS and DFS ----------------

for case_name, goal in cases:

    print("\n===================================")
    print(case_name)
    print("Start : A")
    print("Goal  :", goal)
    print("===================================")

    # BFS
    bfs_path, bfs_nodes = bfs(graph, 'A', goal)

    print("\nBFS")
    print("Path:", " -> ".join(bfs_path))
    print("Nodes Expanded:", bfs_nodes)

    # DFS
    dfs_path, dfs_nodes = dfs(graph, 'A', goal)

    print("\nDFS")
    print("Path:", " -> ".join(dfs_path))
    print("Nodes Expanded:", dfs_nodes)