class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        traversal = []
        self._dfs_helper(start, visited, traversal)
        return traversal

    def _dfs_helper(self, node, visited, traversal):
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in self.graph.get(node, []):
                self._dfs_helper(neighbor, visited, traversal)

# Example usage

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS Traversal starting from node 2:", g.dfs(2))
