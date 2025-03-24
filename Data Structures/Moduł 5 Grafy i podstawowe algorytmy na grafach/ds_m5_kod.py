# Implementacja grafu i BFS
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Graf nieskierowany

    def bfs_shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return None
        visited = set()
        queue = [(start, [start])]
        visited.add(start)
        while queue:
            vertex, path = queue.pop(0)
            if vertex == end:
                return path
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

# Testowanie grafu i BFS
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
path = g.bfs_shortest_path(0, 4)
print("Najkrótsza ścieżka z 0 do 4:", path)  # Wyświetla: [0, 2, 4]