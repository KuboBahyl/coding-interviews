# unidirectional graph
class Graph(object):
    def __init__(self):
        self.vertices = {}

    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present
        if fromVertex in self.vertices:
            self.vertices[fromVertex].append(toVertex)
        else:
            self.vertices[fromVertex] = [toVertex]

    def print_DFS(self, start):
        def collect_rec(node, visited, collected):
            visited[node] = True
            for next_node in self.vertices[node]:
                if not visited[next_node]:
                    collected.append(next_node)
                    collected = collect_rec(next_node, visited, collected)

            return collected

        visited = [False] * len(self.vertices)
        collected = [start]
        return collect_rec(start, visited, collected)

    def print_all_DFS(self):
        for start in self.vertices:
            path = self.print_DFS(start)
            print(path)

    def print_BFS(self, start):
        queue = [start]
        visited = [False] * len(self.vertices)
        collected = []
        while queue:
            temp_node = queue.pop(0)
            collected.append(temp_node)
            visited[temp_node] = True
            for next_node in self.vertices[temp_node]:
                if next_node not in queue and not visited[next_node]:
                    queue.append(next_node)

        return collected

    def print_all_BFS(self):
        for start in self.vertices:
            path = self.print_BFS(start)
            print(path)

    def has_cycle(self, start):
        def search_rec(node, visited):
            visited[node] = True
            for next_node in self.vertices[node]:
                if visited[next_node]:
                    return True
                return search_rec(next_node, visited)
            return False

        visited = [False] * len(self.vertices)
        return search_rec(start, visited)


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 4)
graph.addEdge(1, 0)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(3, 0)
graph.addEdge(2, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(3, 4)
graph.addEdge(4, 1)
graph.addEdge(4, 3)
graph.has_cycle(0)