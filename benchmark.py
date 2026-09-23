import time
from bfs_dfs import bfs, dfs, graph


def run_benchmark(algorithm, start, goal, runs=3):

    times = []
    path = None
    nodes = 0

    for i in range(runs):

        start_time = time.perf_counter()

        path, nodes = algorithm(graph, start, goal)

        end_time = time.perf_counter()

        execution_time = (end_time - start_time) * 1000

        times.append(execution_time)

    average_time = sum(times) / runs

    return path, nodes, average_time


# Test cases
cases = [
    ("Best Case", "B"),
    ("Average Case", "M"),
    ("Worst Case", "Z")
]


print("\n======================================")
print("       BFS vs DFS BENCHMARK")
print("======================================")


for case, goal in cases:

    print("\n--------------------------------------")
    print(case)
    print("Start Node : A")
    print("Goal Node  :", goal)
    print("--------------------------------------")

    # BFS
    bfs_path, bfs_nodes, bfs_time = run_benchmark(
        bfs, "A", goal
    )

    print("\nBFS")
    print("Path           :", " -> ".join(bfs_path))
    print("Nodes Expanded :", bfs_nodes)
    print("Average Time   :", round(bfs_time, 5), "ms")

    # DFS
    dfs_path, dfs_nodes, dfs_time = run_benchmark(
        dfs, "A", goal
    )

    print("\nDFS")
    print("Path           :", " -> ".join(dfs_path))
    print("Nodes Expanded :", dfs_nodes)
    print("Average Time   :", round(dfs_time, 5), "ms")


print("\n======================================")
print("Benchmark completed successfully.")
print("======================================")