import time
from bfs_dfs import bfs, dfs, graph

# Run profiling for 10 seconds
end_time = time.time() + 10

while time.time() < end_time:

    # Run BFS
    bfs(graph, "A", "Z")

    # Run DFS
    dfs(graph, "A", "Z")

print("Profiling completed.")